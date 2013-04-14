__author__ = 'denis'


class UserAnalyzer:
    def __init__(self, repository):
        self.repository = repository

    def get_most_commiters(self):
        nodes = self.repository.get_nodes()
        users = {}
        for node in nodes:
            name = node.get_user()
            if not name in users:
                users[name] = 0
            users[name] += 1
        top = sorted(users.items(), key=lambda x: x[1], reverse=True)
        return top

    def get_most_file_commiters(self):
        nodes = self.repository.get_nodes()
        users = {}
        for node in nodes:
            name = node.get_user()
            if not name in users:
                users[name] = 0
            users[name] += len(node.files())
        top = sorted(users.items(), key=lambda x: x[1], reverse=True)
        return top