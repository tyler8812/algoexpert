def sameBSTs(arrayOne, arrayTwo):
    # O(n^2) time O(n^2) space
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayTwo) == 0 and len(arrayOne) == 0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False

    # O(4n)
    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)

    rightOne = getBiggerOrEqual(arrayOne)
    rightTwo = getBiggerOrEqual(arrayTwo)

    return sameBSTs(leftOne, leftTwo) and sameBSTs(rightOne, rightTwo)


def getSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def getBiggerOrEqual(array):
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual
