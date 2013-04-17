__author__ = 'denis'
from mercurial import util
from mercurial.templatefilters import person


class node:
    def __init__(self, node):
        self.node = node

    def description(self):
        return self.node.description()

    def files(self):
        return self.node.files()

    def get_user(self):
        node_user = self.node.user()
        email = util.email(node_user)
        name = person(node_user)
        return name