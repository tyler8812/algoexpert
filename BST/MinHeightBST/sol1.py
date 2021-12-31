# O(nlog(n)) time O(n) space
# recursive
def constructMinHeightBST(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
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

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
