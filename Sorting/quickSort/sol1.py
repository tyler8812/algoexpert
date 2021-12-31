def quickSort(array):
    # Write your code here.
    # Space O(log(n)) if only choose the samllest subarray every time,
    # the space will be space O(log(n)), think of worst case, because every
    # iteration will get a bigest subarray and length 1 subarray.
    # (n + (1/2n + 1/2n) + (1/4n + 1/4n + 1/4n + 1/4n).....) total for log(n) times
    # Best: O(nlog(n)) time O(log(n)) space
    # Average: O(nlog(n)) time O(log(n)) space
    # Worst: O(n^2) time O(log(n)) space
    quickSortHelper(array, 0, len(array)-1)
    return array


def quickSortHelper(array, start, end):
    if start >= end:
        return
    pivotIdx = start
    leftIdx = start + 1
    rightIdx = end

    while rightIdx >= leftIdx:

        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1

    swap(pivotIdx, rightIdx, array)
    # 	iterate smaller subarray first
    leftSubarrayIsSmaller = rightIdx - 1 - start < end - (rightIdx + 1)
    if leftSubarrayIsSmaller:
        quickSortHelper(array, start, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, end)
    else:
        quickSortHelper(array, rightIdx + 1, end)
        quickSortHelper(array, start, rightIdx - 1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
