"""printparents

Prints statistics about repository
"""
from mercurial import util


def print_statistics(ui, repo, node, **opts):
    # The doc string below will show up in hg help.
    """Print parent information."""
    # repo can be indexed based on tags, an sha1, or a revision number.
    ctx = repo[node]
    try:
        if opts['user']:
            # The string representation of a context returns a smaller portion
            # of the sha1.
            ui.write('Statistics per user')
    except IndexError:
        # Raise an Abort exception if the node has only one parent.
        raise util.Abort('revision %s has only one parent' % node)


cmdtable = {
    # cmd name        function call
    'hgstat': (print_statistics,
        # See mercurial/fancyopts.py for all of the command flag options.
        [('u', 'user', None, 'print statistics per user'),],
        '[options] REV')
}

testedwith = '2.2'