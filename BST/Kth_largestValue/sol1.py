# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(h+k) time O(h) space h: height of tree, k input parameters
# space (recursive stack)


def findKthLargestValueInBst(tree, k):
    info = Info(0, 0)
    treeSearch(tree, info, k)
    return info.value


class Info:
    def __init__(self, visited, value):
        self.visited = visited
        self.value = value


def treeSearch(node, info, k):
    if node is None or info.visited >= k:
        return
    treeSearch(node.right, info, k)
    if info.visited < k:
        info.visited += 1
        info.value = node.value
        treeSearch(node.left, info, k)
