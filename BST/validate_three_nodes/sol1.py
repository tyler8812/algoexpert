# This is an input class. Do not edit.
# O(h) time O(h) space h=hegiht of tree
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
    if node is None:
        return False
    if node is target:
        return True
    if node.value < target.value:
        return isDescendant(target, node.right)
    else:
        return isDescendant(target, node.left)
