"""printparents

Prints statistics about repository
"""
from mercurial import util
from os import path
from datetime import datetime
from mercurial import patch, util
from mercurial.templatefilters import person
def fetch_data_branches(ctx, options):
    yield ctx.branch()
def fetch_data_authors(ctx):
    # data is a dictionnary mapping an author name to the data for
    # this author
    user = ctx.user()
    email = util.email(user)
    name = person(user)
    yield name
def print_statistics(ui, repo, node, **opts):
    # The doc string below will show up in hg help.
    """Print parent information."""
    # repo can be indexed based on tags, an sha1, or a revision number.
    ctx = repo[node]
    try:
        if opts['user']:
            # The string representation of a context returns a smaller portion
            # of the sha1.
            u = fetch_data_authors(ctx)
            for s in u:
                ui.write(s)
            ui.write('Statistics per user')
    except IndexError:
        # Raise an Abort exception if the node has only one parent.
        raise util.Abort('revision %s has only one parent' % node)


