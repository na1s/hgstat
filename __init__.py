def generate_statistic(ui, repo, **opts):
    ui.write('Common repository statistics\r\n')
    ui.write("Heads count:%d\r\n" % len(repo.heads()))
    ui.write("Branches count:%d\r\n" % len(repo.branchtags()))


cmdtable = {
    # cmd name        function call
    'hgstat': (generate_statistic,
               # See mercurial/fancyopts.py for all of the command flag options.
               [('u', 'user', "", 'print statistics per user'), ],
               '[options] REV')
}

testedwith = '2.2'