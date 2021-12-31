# O(n) time O(h) space
def nodeDepths(root):
    depthSum = [0]
    calculateNodeDepth(root, 0, depthSum)
    return depthSum[0]


def calculateNodeDepth(root, currentDepth, depthSum):
    if root is None:
        return

    depthSum[0] += currentDepth

    calculateNodeDepth(root.left, currentDepth+1, depthSum)
    calculateNodeDepth(root.right, currentDepth+1, depthSum)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
