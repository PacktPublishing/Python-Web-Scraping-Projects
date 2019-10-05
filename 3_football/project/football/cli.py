import json
from pathlib import Path

import click
from click import echo
from football.crawler import BBCFootballCrawler
from football.monitor import Monitor
from football.notifiers import EmailNotifier, SlackNotifier

# setup application constants
APP_NAME = 'football-monitor'
APP_DIR = Path(click.get_app_dir(APP_NAME))
APP_DIR.mkdir(exist_ok=True, parents=True)
DATA_FILE = APP_DIR / ('crawl_data' + '.json')
DATA_FILE.touch(exist_ok=True)
HISTORY_FILE = APP_DIR / (APP_NAME + '.history')
HISTORY_FILE.touch(exist_ok=True)


@click.group()
@click.pass_context
def main(ctx):
    """Football data crawler and notifier"""
    ctx.obj = {}


def read_data(path):
    """Load data from local data file"""
    with open(path, 'r') as f:
        contents = f.read()
        if contents:
            return json.loads(contents)
        else:
            return {'upcoming': [], 'recent': []}


@main.command('crawl')
@click.argument('teams', nargs=-1)
@click.option('--file', default=DATA_FILE, show_default=True,
              help='filepath to where to store data, appending new crawl results')
def crawl(teams, file):
    """Crawl upcoming and recent games of supplied team names"""
    old_results = read_data(file)
    echo(f"Crawling teams: {', '.join(teams)}")
    with open(file, 'w') as f:
        new_results = BBCFootballCrawler(teams).crawl()
        # combine both old and new results and keep unique values
        results = {
            'recent': list({v['id']: v for v in new_results['recent'] + old_results['recent']}.values()),
            'upcoming': list({v['id']: v for v in new_results['upcoming'] + old_results['upcoming']}.values()),
        }
        f.write(json.dumps(results, indent=2))
    new_recent_count = len(results['recent']) - len(old_results['recent'])
    new_upcoming_count = len(results['upcoming']) - len(old_results['upcoming'])
    echo(f"Found new {new_recent_count} recent and {new_upcoming_count} upcoming matches")


@main.group('monitor')
@click.option('--file', default=DATA_FILE, show_default=True,
              help='filepath to where data is stored')
@click.option('--history-file', default=HISTORY_FILE, show_default=True,
              help='where history cache is stored')
@click.pass_obj
def monitor(obj, file, history_file):
    """Check crawled data for something to notify"""
    obj['file'] = file
    obj['history_file'] = history_file


@monitor.command('slack')
@click.argument('channel')
@click.argument('slackhook')
@click.pass_obj
def monitor_slack(obj, channel, slackhook):
    """send monitor results to a slack channel"""
    notifier = SlackNotifier(slackhook, channel)
    data = read_data(obj['file'])
    monitor = Monitor([notifier], history_file=obj['history_file'])
    found_recent = monitor.check_upcoming(data['recent'])
    found_upcoming = monitor.check_upcoming(data['upcoming'])
    echo(f'found {len(found_recent)} recent and '
         f'{len(found_upcoming)} upcoming results and '
         f'sent out to slack channel {channel}')


@monitor.command('email')
@click.argument('emails')
@click.option('-e', 'email', help='senders email', required=True)
@click.option('-P', 'password', help='email password', required=True)
@click.option('-s', 'server', help='email server', default='smtp.gmail.com', show_default=True)
@click.option('-p', 'port', help='email port', default=465, type=click.INT, show_default=True)
@click.pass_obj
def monitor_email(obj, emails, server, port, email, password):
    """send monitor results to provided list of emails (comma separated)"""
    emails = emails.split(',')
    data = read_data(obj['file'])
    notifier = EmailNotifier(server, port, email, password, emails)
    monitor = Monitor([notifier], history_file=obj['history_file'])
    found_recent = monitor.check_upcoming(data['recent'])
    found_upcoming = monitor.check_upcoming(data['upcoming'])
    echo(f'found {len(found_recent)} recent and {len(found_upcoming)} upcoming results and sent out email to: {emails}')
