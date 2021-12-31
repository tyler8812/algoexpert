def firstDuplicateValue(array):
    # O(n) time O(1) space
    for value in array:
        absValue = abs(value)
        if array[absValue-1] < 0:
            return absValue
        else:
            array[absValue-1] *= -1
    return -1
