def findClosestValueInBst(tree, target):
    # Avg: O(log(n)) time n is number of all node in tree
    # Worst: O(n) if tree only have one branch
    # O(1) space
    return findClosestValueInBstHelper(tree, target)


def findClosestValueInBstHelper(tree, target):
    currentNode = tree
    closest = float("inf")
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
