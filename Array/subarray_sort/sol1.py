array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]


def subarraySort(array):
    # O(nlog(n)) time O(n)space
    sortedArray = array.copy()
    sortedArray.sort()

    first = -1
    last = -1
    for i in range(len(sortedArray)):
        if sortedArray[i] != array[i]:
            first = i
            break
    for j in range(len(sortedArray)-1, -1, -1):
        if sortedArray[j] != array[j]:
            last = j
            break

    return [first, last]


print(subarraySort(array))
