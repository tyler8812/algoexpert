# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    three_largest = [None, None, None]
    for num in array:
        update_largest(three_largest, num)

    return three_largest


def update_largest(array, num):
    if array[2] is None or num > array[2]:
        shift_and_update(array, num, 2)
    elif array[1] is None or num > array[1]:
        shift_and_update(array, num, 1)
    elif array[0] is None or num > array[0]:
        shift_and_update(array, num, 0)


def shift_and_update(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array))
