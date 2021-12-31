# This is an input class. Do not edit.
# O(n) time O(h) space
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, isBalanced, height):
        self.height = height
        self.isBalanced = isBalanced


def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)
    leftTree = getTreeInfo(node.left)
    rightTree = getTreeInfo(node.right)

    isBalanced = leftTree.isBalanced and rightTree.isBalanced and abs(
        leftTree.height - rightTree.height) <= 1

    height = max(leftTree.height, rightTree.height) + 1
    return TreeInfo(isBalanced, height)
