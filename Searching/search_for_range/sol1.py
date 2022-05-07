# O(log(n)) time | O(1) space
def searchForRange(array, target):
    final_range = [-1, -1]
    binary_search(array, target, 0, len(array) - 1, final_range, True)
    binary_search(array, target, 0, len(array) - 1, final_range, False)
    return final_range


def binary_search(array, target, left, right, final_range, go_left):

    while left <= right:
        print(left, right)
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        else:
            if go_left:
                if mid == 0 or array[mid - 1] != target:
                    final_range[0] = mid
                    return
                else:
                    right = mid - 1
            else:
                if mid == len(array) - 1 or array[mid + 1] != target:
                    final_range[1] = mid
                    return
                else:
                    left = mid + 1


input = {"array": [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], "target": 45}
print(searchForRange(input["array"], input["target"]))
