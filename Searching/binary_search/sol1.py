# O(log(n)) time | O(1) space
def binarySearch(array, target):
    start_index = 0
    end_index = len(array) - 1

    while True:
        current_index = (start_index + end_index) // 2
        if start_index > end_index:
            return -1
        if target > array[current_index]:
            start_index = current_index + 1
        elif target < array[current_index]:
            end_index = current_index - 1
        else:
            return current_index


test = {"array": [0, 1, 21, 34, 45, 45, 61, 71, 72, 73], "target": 0}

print(binarySearch(test["array"], test["target"]))
