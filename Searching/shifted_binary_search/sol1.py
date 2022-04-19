# O(log(n)) time | O(1) space
def shiftedBinarySearch(array, target):

    left_idx = 0
    right_idx = len(array) - 1
    while left_idx <= right_idx:
        current_idx = (left_idx + right_idx) // 2
        current_value = array[current_idx]
        left_value = array[left_idx]
        right_value = array[right_idx]
        if current_value == target:
            return current_idx
        elif right_value <= current_value:
            if target < current_value and target >= left_value:
                right_idx = current_idx - 1
            else:
                left_idx = current_idx + 1
        else:
            if target > current_value and target <= right_value:
                left_idx = current_idx + 1
            else:
                right_idx = current_idx - 1

    return -1
