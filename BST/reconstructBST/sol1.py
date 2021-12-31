# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # O(n^2) time O(h) space h recursive call stack(height of binary tree)
    # O(n) space while needs to output the final BST
    if len(preOrderTraversalValues) == 0:
        return None

    currentValue = preOrderTraversalValues[0]
    rightSubTreeRootIdx = len(preOrderTraversalValues)

    for idx in range(1, len(preOrderTraversalValues)):
        value = preOrderTraversalValues[idx]
        if value >= currentValue:
            rightSubTreeRootIdx = idx
            break

    leftSubTree = reconstructBst(
        preOrderTraversalValues[1:rightSubTreeRootIdx])
    rightSubTree = reconstructBst(
        preOrderTraversalValues[rightSubTreeRootIdx:])
    return BST(currentValue, leftSubTree, rightSubTree)
