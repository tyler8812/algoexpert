array = [1, 2, 3, 4, 5, -1]


def subarraySort(array):
    # O(n) time O(1) space
    # found all unsort number
    minOutOfOuder = float("inf")
    maxOutOfOuder = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if isOutOfOuder(i, num, array):
            minOutOfOuder = min(minOutOfOuder, num)
            maxOutOfOuder = max(maxOutOfOuder, num)

    if minOutOfOuder == float("inf"):
        return [-1, -1]

    # compare the max and min from left and right index
    subArrayLeftIdx = 0
    while minOutOfOuder >= array[subArrayLeftIdx]:
        subArrayLeftIdx += 1
    subArrayRightIdx = len(array)-1
    while maxOutOfOuder <= array[subArrayRightIdx]:
        subArrayRightIdx -= 1
    return [subArrayLeftIdx, subArrayRightIdx]


def isOutOfOuder(i, num, array):
    if i == 0:
        return num > array[i+1]
    if i == len(array)-1:
        return num < array[i-1]

    return num > array[i+1] or num < array[i-1]


print(subarraySort(array))
