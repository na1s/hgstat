__author__ = 'denis'


class Branch:
    def __init__(self, name, status):
        self.status = status
        self.name = name
    def status(self):
        return self.status
    def get_name(self):
        return self.name