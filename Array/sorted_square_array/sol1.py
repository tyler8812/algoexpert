def sortedSquaredArray(array):
    # Write your code here.
    # O(nlog(n)) time O(n) space
    for idx in range(len(array)):
        array[idx] = array[idx] * array[idx]

    array.sort()
    return array
