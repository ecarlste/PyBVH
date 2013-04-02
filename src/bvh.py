__author__ = 'Erik S Carlsten'


class BVH:
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def _read_hierarchy(self):
        pass


class Joint:
    def __init__(self, name, offset_x, offset_y, offset_z):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)