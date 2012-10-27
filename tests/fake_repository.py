__author__ = 'denis'
from mercurial import patch, util
class FakeRepository:

    def create(self, ui, reponame):
        None

    def add_file(self, ui, repo, filename):
        None

    def commit_file(self, ui, repo, filename, message = '', user = '', date = ''):
        None