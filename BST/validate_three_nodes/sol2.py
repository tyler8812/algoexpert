# This is an input class. Do not edit.
# O(h) time O(1) space h=hegiht of tree
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    if isDescendant(nodeOne, nodeTwo):
        return isDescendant(nodeTwo, nodeThree)
    if isDescendant(nodeThree, nodeTwo):
        return isDescendant(nodeTwo, nodeOne)
    return False


def isDescendant(target, node):
    while node is not None and node is not target:
        node = node.right if node.value < target.value else node.left
    return node is target
