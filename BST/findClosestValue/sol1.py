def findClosestValueInBst(tree, target):
    # Avg: O(log(n)) time n is number of all node in tree
    # Worst: O(n) if tree only have one branch
    # space is the same as time if you use recursive(adding call stack)
    return findClosestValueInBstHelper(tree, target, float("inf"))


def findClosestValueInBstHelper(tree, target, closest):

    # stop at bottom
    if tree is None:
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return target


# This is the class of the input tree. Do not edit.
class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
