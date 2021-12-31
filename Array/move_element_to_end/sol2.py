def moveElementToEnd(array, toMove):
    # Write your code here.
    # O(n) time	O(1) space
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] != toMove:
            i += 1
        else:
            if array[j] == toMove:
                j -= 1
            else:
                array[i], array[j] = array[j], array[i]

    return array
