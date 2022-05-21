# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space


def selectionSort(array):
    current_idx = 0
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        swap(array, smallest_idx, current_idx)
        current_idx += 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
