# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def bubbleSort(array):
    for i in reversed(range(len(array))):
        for j in range(0, i):
            if array[j + 1] < array[j]:
                swap(array, j, j + 1)

    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]
print(bubbleSort(array=array))
