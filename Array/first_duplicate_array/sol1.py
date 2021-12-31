def firstDuplicateValue(array):
    # Write your code here.
    # O(n^2) time O(1) space
    smallestIdx = len(array)
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                if smallestIdx > j:
                    smallestIdx = j
                    print(j)

    if smallestIdx == len(array):
        return -1

    return array[smallestIdx]
