def largestRange(array):
    # O(n) time O(n) space
    bestRange = []
    longestlength = 0
    dict = {}
    for i in array:
        if i not in array:
            dict[i] = True

    for i in dict:
        if dict[i]:
            dict[i] = False
            currentLength = 1
            left = i - 1
            right = i + 1
            while left in dict:
                dict[left] = False
                currentLength += 1
                left -= 1
            while right in dict:
                dict[right] = False
                currentLength += 1
                right += 1

        if currentLength > longestlength:
            longestlength = currentLength
            bestRange = [left+1, right-1]

    return bestRange
