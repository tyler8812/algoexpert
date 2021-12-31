# O(nlog(n)) time O(n) space
# recursive
def constructMinHeightBST(array, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]

    bst = BST(valueToAdd)

    bst.left = constructMinHeightBST(array, startIdx, midIdx-1)
    bst.right = constructMinHeightBST(array, midIdx+1, endIdx)
    return bst


def minHeightBst(array):
    return constructMinHeightBST(array, 0, len(array)-1)


class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
