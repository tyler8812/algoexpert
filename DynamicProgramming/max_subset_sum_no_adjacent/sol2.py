# O(n) time O(1) space
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        pre1 = max(array[0], array[1])
        pre2 = array[0]
        for i in range(2, len(array)):
            temp = pre1
            pre1 = max(pre2 + array[i], pre1)
            pre2 = temp
        return pre1
