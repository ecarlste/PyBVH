__author__ = 'Erik S Carlsten'


class BVH:
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def _read_hierarchy(self):
        pass

    def _read_motion(self):
        pass


class Joint:
    def __init__(self, name, offset_x, offset_y, offset_z, channels):
        self.name = name
        self.offset.x = offset_x
        self.offset.y = offset_y
        self.offset.z = offset_z
        self.channels = channels
        self.children = []

    def add_child(self, child):
        self.children.append(child)