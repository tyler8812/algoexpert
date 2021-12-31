array = [1, 2]


def subarraySort(array):
    # O(n) time O(1) space
    prev = array[0]
    tempFirst = -1
    for i in range(1, len(array)):
        if tempFirst == -1:
            if prev > array[i]:
                tempFirst = array[i]
            prev = array[i]
        else:
            if tempFirst > array[i]:
                tempFirst = array[i]
    print(tempFirst)

    if tempFirst != -1:
        for i in range(0, len(array)):
            if tempFirst < array[i]:
                tempFirst = i
                break

    next = array[-1]
    tempLast = -1
    for i in range(len(array)-2, -1, -1):
        if tempLast == -1:
            if next < array[i]:
                tempLast = array[i]
            next = array[i]
        else:
            if tempLast < array[i]:
                tempLast = array[i]

    print(tempLast)

    if tempLast != -1:
        for i in range(len(array)-1, -1, -1):
            if tempLast > array[i]:
                tempLast = i
                break

    return [tempFirst, tempLast]


print(subarraySort(array))
