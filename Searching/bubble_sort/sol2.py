# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def bubbleSort(array):
    is_sorted = False
    count = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - count):
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                is_sorted = False
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
