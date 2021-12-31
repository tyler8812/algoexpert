# O(n) time O(n) space
# recursive
def constructMinHeightBST(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    newBst = BST(valueToAdd)
    if bst is None:
        bst = newBst
    else:
        if array[midIdx] < bst.value:
            bst.left = newBst
            bst = bst.left
        else:
            bst.right = newBst
            bst = bst.right

    constructMinHeightBST(array, bst, startIdx, midIdx-1)
    constructMinHeightBST(array, bst, midIdx+1, endIdx)
    return bst


def minHeightBst(array):
    return constructMinHeightBST(array, None, 0, len(array)-1)


class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
