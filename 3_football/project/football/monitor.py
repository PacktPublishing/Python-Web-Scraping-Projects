from datetime import timedelta, datetime, timezone


class Monitor:
    """Monitors matches file and sends out notifications if necessary"""

    def __init__(self, notifiers, history_file, max_age=timedelta(days=3)):
        self.history_file = history_file
        self.notifiers = notifiers
        self.history = self.read_history()
        self.max_age = max_age

    def read_history(self):
        try:
            with open(self.history_file) as f:
                return [line.strip() for line in f.readlines()]
        except FileNotFoundError:
            return []

    def check_recent(self, data):
        new_items = self.check_matches(data)
        if new_items:
            subject = f'results of recent {len(new_items)} games'
            self.notify(new_items, subject)
        return new_items

    def check_upcoming(self, data):
        new_items = self.check_matches(data)
        if new_items:
            subject = f'found {len(new_items)} new games'
            self.notify(new_items, subject)
        return new_items

    def check_matches(self, data):
        new_items = []
        for match in data:
            id_ = match['id']
            if id_ in self.history:
                continue
            # skip items that are too old to monitor
            start_time = datetime.strptime(match['start_time'], '%Y-%m-%dT%H:%M:%S%z')
            if start_time + self.max_age < datetime.now(timezone.utc):
                continue
            new_items.append(match)
            self.history.append(id_)
        self.save_history()
        return new_items

    def notify(self, items, subject):
        for notifier in self.notifiers:
            notifier.notify(items, subject)

    def save_history(self):
        with open(self.history_file, 'w') as f:
            f.write('\n'.join(self.history).strip())
