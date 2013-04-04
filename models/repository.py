from branch import Branch

__author__ = 'denis'


class Repository:
    def __init__(self, repo):
        self.repo = repo

    def get_heads(self):
        return self.repo.heads()

    def get_branches(self):
        heads = self.repo.heads()
        status = ""
        branches = []
        for b, n in self.repo.branchtags().iteritems():
            if not self.repo.branchheads(b):
                status = 'closed'
            elif n not in heads:
                status = 'inactive'
            else:
                status = 'open'
            branches.append(Branch(self,b,n, status))
        return branches