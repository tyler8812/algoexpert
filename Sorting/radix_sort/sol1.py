# O(d * (n+b)) time O(n+b) space
# n: length of array
# d: max number of digit
# b the base of the number system
def radixSort(array):
    if len(array) == 0:
        return []
    digit = 0
    # O(n) time
    max_number = max(array)
    while max_number // (10 ** digit) > 0:
        counting_sort(array, digit)
        digit += 1
    return array


def counting_sort(array, digit):
    count_array = [0] * 10
    sorted_array = [0] * len(array)

    for value in array:
        count_idx = (value // (10 ** digit)) % 10
        count_array[count_idx] += 1
    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for i in reversed(range(len(array))):
        count_idx = (array[i] // (10 ** digit)) % 10
        count_array[count_idx] -= 1
        sorted_array[count_array[count_idx]] = array[i]

    for i in range(len(array)):
        array[i] = sorted_array[i]
