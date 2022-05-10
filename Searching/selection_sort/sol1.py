# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selectionSort(array):
    for i in range(len(array)):
        min = float("inf")
        min_idx = -1
        for j in range(i, len(array)):
            if array[j] < min:
                min_idx = j
                min = array[j]
        swap(array, min_idx, i)

    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
