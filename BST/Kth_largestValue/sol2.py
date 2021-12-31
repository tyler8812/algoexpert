# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time O(n) sapce
# search all the node in tree and get kth largest value
def findKthLargestValueInBst(tree, k):
    nodes = []
    treeSearch(tree, nodes)
    return nodes[len(nodes)-k]


def treeSearch(node, nodes):
    if node.left is not None:
        treeSearch(node.left, nodes)
    nodes.append(node.value)
    if node.right is not None:
        treeSearch(node.right, nodes)
