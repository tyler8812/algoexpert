# O(n) time O(d) sapce
def invertBinaryTree(tree):
    stack = [tree]
    while len(stack):
        current = stack.pop()
        if current is None:
            continue
        swapLeftRight(current)
        stack.append(current.left)
        stack.append(current.right)
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def swapLeftRight(node):
    node.right, node.left = node.left, node.right
