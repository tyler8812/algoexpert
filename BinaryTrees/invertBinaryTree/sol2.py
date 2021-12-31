# O(n) time O(d) sapce
def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree


class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def swapLeftRight(node):
    node.right, node.left = node.left, node.right
