# This is an input class. Do not edit.
# O(h) time O(h) call stack
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
        return getLeftMostChild(node.right)

    return getRightMostParent(node)


def getLeftMostChild(node):
    if node.left is not None:
        return getLeftMostChild(node.left)
    else:
        return node


def getRightMostParent(node):
    if node.parent is None:
        return None
    elif node.parent.left == node:
        return node.parent
    else:
        return getRightMostParent(node.parent)
