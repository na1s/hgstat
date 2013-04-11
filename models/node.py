__author__ = 'denis'
class node:
    def __init__(self, node):
        self.node = node
    def description(self):
        return self.node.description()
    def files(self):
        return self.node.files()