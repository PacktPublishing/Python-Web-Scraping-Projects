import json
from collections import defaultdict
from typing import Dict
from urllib.parse import urljoin

import requests
from parsel import Selector


class BBCFootballCrawler:
    """Crawler for football match infomation displayed on bcc.com/sport/football"""
    team_directory_url = 'https://www.bbc.com/sport/football/teams'

    def __init__(self, teams):
        self.teams = [team.lower() for team in teams]

    @classmethod
    def from_file(cls, filename):
        """Create class from teams file that has 1 team name per line"""
        teams = []
        with open(filename) as file:
            for line in file:
                if not line.strip():  # skip empty lines
                    continue
                teams.append(line.strip())
        return cls(teams)

    def crawl(self) -> Dict:
        """
        Crawls football teams for their recent information about upcoming and past matches
        returns dictionary of upcoming, recent matches:
        {"upcoming":
            [{match information},...],
        "recent":
            [{match infortmation},...],
        }
        """
        session = requests.Session()
        team_resp = session.get(self.team_directory_url)
        team_sel = Selector(text=team_resp.text)
        found_teams = []
        results = {'upcoming': [], 'recent': []}
        teams = team_sel.css('#all-teams .gs-o-list-ui__item a')
        for team in teams:
            name = team.xpath('text()').extract_first().lower().strip()
            if name not in self.teams:
                continue
            found_teams.append(name)
            url = team.xpath('@href').extract_first()
            team_data = self.crawl_team(url, session)
            results['upcoming'].extend(team_data['upcoming'])
            results['recent'].extend(team_data['recent'])
        session.close()

        # check if there were teams configured that are not found on the page
        missed_teams = set(self.teams) - set(found_teams)
        if missed_teams:
            raise NotImplementedError(f'Unsupported teams requested: {missed_teams}')
        return results

    def crawl_team(self, url, session) -> dict:
        """
        Crawl team page url and return upcoming and recent matches:
        {
            "upcoming": [{}...],
            "recent": [{},...],
        }
        """
        resp = session.get(url)
        sel = Selector(text=resp.text)
        # regex pattern used to identify <script> that contains data json
        script = 'payloads.push.+?scores-tabbed-teams-model'
        regex = r', ({.+?})\);'  # 2nd js function argument that is json
        data = sel.xpath(f"//script[re:test(text(), '{script}')]").re(regex)
        data = json.loads(data[0])

        parsed = defaultdict(list)

        def parse_event(event):
            """parse base even details for upcoming and recent events"""
            event_data = {
                'tournament': event['tournamentName']['full'],
                'start_time': event['startTime'],
                'team_home': event['homeTeam']['name']['full'],
                'team_away': event['awayTeam']['name']['full'],
                'venue': event['venue']['name']['full'],
            }
            # create unique match id from event data
            event_data['id'] = ':'.join(event_data[k] for k in ['team_home', 'team_away', 'start_time'])
            return event_data

        # parse upcoming games
        for round_ in data['body']['fixtures']['body']['rounds']:
            for event in round_['events']:
                parsed['upcoming'].append(parse_event(event))
        # parse past games
        for round_ in data['body']['results']['body']['rounds']:
            for event in round_['events']:
                parsed['recent'].append({
                    **parse_event(event),
                    'team_home_score': event['homeTeam']['scores']['score'],
                    'team_away_score': event['homeTeam']['scores']['score'],
                    'time': event['minutesElapsed'] + event['minutesIntoAddedTime'],
                    'attendance': event['attendance'],
                    'url': urljoin(url, event['href']),
                })
        return parsed
