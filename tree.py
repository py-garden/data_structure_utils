class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.children = []
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1
        self.path = [] if parent is None else parent.path + [parent]

    def add_child(self, child_node):
        child_node.parent = self
        child_node.depth = self.depth + 1
        child_node.path = self.path + [self]
        self.children.append(child_node)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.data) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


# Generic collect function using metadata from node
def collect(node, predicate):
    results = []

    if predicate(node):
        results.append(node)

    for child in node.children:
        results.extend(collect(child, predicate))

    return results
