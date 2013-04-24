from time import *

from mercurial.node import hex, nullid
from analyzers.files import FileAnalyzer
from analyzers.users import UserAnalyzer
from models.repository import *
from reporters.google_charts.user_charts import UserCharts


def generate_statistic(ui, repo, **opts):
    ui.write('Common repository statistics\r\n')
    current_repo = Repository(repo)
    branches = current_repo.get_branches()

    ui.write("Heads count:%d\r\n" % len(repo.heads()))
    ui.write("Branches count:%d\r\n" % len(branches))
    ui.write("Open branches count:%d\r\n" % len([b for b in branches if b.status == "open"]))
    user_analyzer = UserAnalyzer(current_repo)
    file_analyzer = FileAnalyzer(current_repo)
    stat = user_analyzer.get_most_commiters()
    #stat2 = user_analyzer.get_most_file_commiters()
    #stat3 = file_analyzer.get_most_changed_files()
    c = UserCharts()
    c.get_most_comitters(stat)
cmdtable = {
    # cmd name        function call
    'hgstat': (generate_statistic,
               # See mercurial/fancyopts.py for all of the command flag options.
               [('u', 'user', "", 'print statistics per user'), ],
               '[options] REV')
}

testedwith = '2.2'