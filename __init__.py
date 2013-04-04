from mercurial.node import hex, nullid
from models.Repository import *


def generate_statistic(ui, repo, **opts):
    ui.write('Common repository statistics\r\n')
    current_repo = Repository(repo)
    branches = current_repo.get_branches()

    ui.write("Heads count:%d\r\n" % len(repo.heads()))
    ui.write("Branches count:%d\r\n" % len(branches))
    ui.write("Open branches count:%d\r\n" % len([b for b in branches if b.status == "open"]))


cmdtable = {
    # cmd name        function call
    'hgstat': (generate_statistic,
               # See mercurial/fancyopts.py for all of the command flag options.
               [('u', 'user', "", 'print statistics per user'), ],
               '[options] REV')
}

testedwith = '2.2'