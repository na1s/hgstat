__author__ = 'denis'

class FakeRepository:

    def create(self, ui, reponame):
        return mercurial.hg.repository(ui, reponame, create = 1)

    def add(self, ui, repo, filename):
        mercurial.commands.add(ui, repo, filename)

    def commit(self, ui, repo, filename, message = '', user = '', date = ''):
        if not message:
            message = 'Added %s.' % filename
        if not user:
            user = 'jdoe'
        if not date:
            date = str(int(time.time())) + ' 0'
        mercurial.commands.commit(ui, repo, filename, message = message, user = user, date = date)