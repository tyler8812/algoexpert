class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.rgiht = None


# O(n) time O(n) space
def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums


def calculateBranchSums(node, currentSum, sums):
    if node is None:
        return

    currentSum = currentSum + node.value

    if node.left is None and node.right is None:
        sums.append(currentSum)
        return

    calculateBranchSums(node.left, currentSum, sums)
    calculateBranchSums(node.right, currentSum, sums)
