from time import gmtime
from mercurial import util
from os import path
from datetime import datetime
from mercurial import patch, util
from mercurial.templatefilters import person
__author__ = 'denis'


class Branch:
    def __init__(self,repository, name, node, status):
        self.status = status
        self.name = name
        self.node = node
        self.repository = repository

    def status(self):
        return self.status
    def get_name(self):
        return self.name
    def get_node(self):
        return self.node
    def get_date(self):
        mercurial_date = self.repository.repo[self.get_node()].date()[0]
        date = gmtime(mercurial_date)
        return date
    def get_user(self):
        node_user = self.repository.repo[self.get_node()].user()
        email = util.email(node_user)
        name = person(node_user)
        return name,email