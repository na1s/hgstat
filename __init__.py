from time import *

from mercurial.node import hex, nullid
from models.repository import *
def generate_statistic(ui, repo, **opts):
    ui.write('Common repository statistics\r\n')
    current_repo = Repository(repo)
    branches = current_repo.get_branches()

    ui.write("Heads count:%d\r\n" % len(repo.heads()))
    ui.write("Branches count:%d\r\n" % len(branches))
    ui.write("Open branches count:%d\r\n" % len([b for b in branches if b.status == "open"]))
    files = {}
    for b in branches:
        date_str = strftime("%Y-%m-%d %H:%M:%S", b.get_date())
        print b.get_user()
        ui.write("Branch : %s, Date:%s\r\n" % (b.get_name(), date_str))
        nodes = b.get_nodes()

        for node in nodes:
            for file in node.files():
                if not file in files:
                    files[file]=0
                files[file]+=1
    top = sorted(files.items(), key=lambda x: x[1],reverse = True)
    print top[0:30]

cmdtable = {
    # cmd name        function call
    'hgstat': (generate_statistic,
               # See mercurial/fancyopts.py for all of the command flag options.
               [('u', 'user', "", 'print statistics per user'), ],
               '[options] REV')
}

testedwith = '2.2'