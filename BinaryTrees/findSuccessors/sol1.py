# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    inOrderList = getInOrederTraversal(tree, [])

    for idx, currentNode in enumerate(inOrderList):
        if currentNode != node:
            continue
        if idx == len(inOrderList) - 1:
            return None
        return inOrderList[idx+1]


def getInOrederTraversal(node, order):
    if node is None:
        return

    getInOrederTraversal(node.left, order)
    order.append(node)
    getInOrederTraversal(node.right, order)

    return order
