import smtplib
import ssl

import requests


class SlackNotifier:
    """
    This is a monitor for Slack messaging service
    It uses slack webhook app that can be found here:
    https://slack.com/apps/A0F7XDUAZ-incoming-webhooks
    """

    def __init__(self, hook_url, channel, name='bot', avatar=':robot_face:'):
        """
        :param hook_url: hook url
        :param name: displayed name for sent messages
        :param avatar: displayed avatar for sent messages
        """
        self.hook_url = hook_url
        self.name = name
        self.avatar = avatar
        self.channel = channel

    def notify(self, matches, subject):
        body = ''
        for match in matches:
            body += f"\n{match['team_home']} vs {match['team_home']} at {match['start_time']}"
            if 'url' in match:
                body += f" more at {match['url']}"
        self.send_msg(f'{subject}\n\n{body.strip()}', )

    def send_msg(self, text):
        """Send a message to channel"""
        data = {
            'channel': self.channel,
            'text': text,
            'link_names': '1',
            'username': self.name,
            'icon_emoji': self.avatar,
        }
        return requests.post(self.hook_url, json=data)


class EmailNotifier:
    """
    Email notifier requires some a smtp server, for example if you have a
    gmail.com account you can use:
        e = EmailNotifier('smtp.gmail.com', 465, 'you@gmail.com', 'password')
        e.send_email(['wraptile@pm.me'], 'this subject\n\nthis is body!')
    """

    def __init__(self, server, port, sender_email, password, receiver_emails):
        context = ssl.create_default_context()
        self.sender_email = sender_email
        self.receiver_emails = receiver_emails
        self.server = smtplib.SMTP_SSL(server, port, context=context)
        self.server.login(sender_email, password)

    def notify(self, matches, subject):
        body = ''
        for match in matches:
            body += f"\n{match['team_home']} vs {match['team_away']} at {match['start_time']}"
            if 'url' in match:
                body += f" more at {match['url']}"
        self.send_email(subject, body.strip(), self.receiver_emails)

    def send_email(self, subject, message, to):
        header = f"From: {self.sender_email}\nTo: {','.join(self.receiver_emails)}\nSubject: {subject}"
        return self.server.sendmail(self.sender_email, to, header + '\n\n' + message)
