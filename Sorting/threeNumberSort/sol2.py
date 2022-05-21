def threeNumberSort(array, order):
    first_value = order[0]
    third_value = order[2]

    first_idx = 0

    for i in range(len(array)):
        if array[i] == first_value:
            array[i], array[first_idx] = array[first_idx], array[i]
            first_idx += 1
    last_idx = len(array) - 1
    for i in range(len(array) - 1, -1, -1):
        if array[i] == third_value:
            array[i], array[last_idx] = array[last_idx], array[i]
            last_idx -= 1

    return array
