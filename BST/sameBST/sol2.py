def sameBsts(arrayOne, arrayTwo):
    # O(n^2) time O(d) space
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minValue, maxValue):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxTwo == rootIdxOne
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minValue)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(
        arrayOne, rootIdxOne, maxValue)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minValue)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(
        arrayTwo, rootIdxTwo, maxValue)

    currentValue = arrayOne[rootIdxOne]
    leftAreSame = areSameBsts(
        arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minValue, currentValue)
    rightAreSame = areSameBsts(
        arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxValue)
    return leftAreSame and rightAreSame


def getIdxOfFirstSmaller(array, startingIdx, minValue):
    for i in range(startingIdx+1, len(array)):
        if array[i] < array[startingIdx] and array[i] >= minValue:
            return i
    return -1


def getIdxOfFirstBiggerOrEqual(array, startingIdx, maxValue):
    for i in range(startingIdx+1, len(array)):
        if array[i] >= array[startingIdx] and array[i] < maxValue:
            return i
    return -1
