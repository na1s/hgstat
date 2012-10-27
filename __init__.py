def generate_statistic(ui, repo, node, **opts):
    ctx = repo[node]
    ui.write('Statistics per user')

cmdtable = {
    # cmd name        function call
    'hgstat': (generate_statistic,
               # See mercurial/fancyopts.py for all of the command flag options.
               [('u', 'user', None, 'print statistics per user'),],
               '[options] REV')
}

testedwith = '2.2'