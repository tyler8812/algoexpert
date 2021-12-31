# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, rootIdx) -> None:
        self.rootIdx = rootIdx


def reconstructBst(preOrderTraversalValues):
    # O(n) time O(h) space recursion call stack
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)


def reconstructBstFromRange(lower, upper, array, treeInfo):
    if treeInfo.rootIdx == len(array):
        return None
    rootValue = array[treeInfo.rootIdx]
    if rootValue < lower or rootValue >= upper:
        return None
    treeInfo.rootIdx += 1
    leftSubTree = reconstructBstFromRange(lower, rootValue, array, treeInfo)
    rightSubTree = reconstructBstFromRange(rootValue, upper, array, treeInfo)
    return BST(rootValue, leftSubTree, rightSubTree)
