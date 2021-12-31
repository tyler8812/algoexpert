def firstDuplicateValue(array):
    # O(n) time O(n) space
    dictionary = {}
    for i in array:
        if i in dictionary:
            return i
        else:
            dictionary[i] = True
    return -1
