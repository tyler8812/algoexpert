
def largestRange(array):
    # O(n) time O(n) space
    dict = {}
    # add all number to a dictionary
    for i in array:
        if i not in dict:
            dict[i] = 1
    print(dict)
    max_key = float("-inf")
    min_key = float("inf")
    # find max_key min_key
    for i in dict:
        if i < min_key:
            min_key = i
        if i > max_key:
            max_key = i

    maxLength = -1
    maxLengthFirst = -1
    maxLengthLast = len(array)
    tempLength = -1
    for i in range(min_key, max_key+1):
        if i in dict:
            if tempLength == -1:
                tempLength = 1
            else:
                tempLength += 1

            if tempLength > maxLength:
                maxLength = tempLength
                maxLengthFirst = i - tempLength + 1
                maxLengthLast = i

        else:
            tempLength = -1
    return([maxLengthFirst, maxLengthLast])
