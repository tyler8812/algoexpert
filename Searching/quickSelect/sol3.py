def quickselect(array, k):
    # Write your code here.
    # # (n + (1/2n) + (1/4n).....) = 2n
    # best: O(n) time O(1) space
    # avg: O(n) O(1) space
    # worst: O(n^2) O(1) space
    # using quick sort
    position = k - 1
    return quickSelectHelper(array, 0, len(array) - 1, position)


def quickSelectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception("error")
        pivot = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx

        while leftIdx <= rightIdx:
            if array[pivot] < array[leftIdx] and array[pivot] > array[rightIdx]:
                swap(array, leftIdx, rightIdx)
            if array[pivot] >= array[leftIdx]:
                leftIdx += 1
            if array[pivot] <= array[rightIdx]:
                rightIdx -= 1
        swap(array, pivot, rightIdx)
        if position == rightIdx:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
