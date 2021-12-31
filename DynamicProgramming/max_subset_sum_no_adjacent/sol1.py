# O(n) time O(n) space
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return max(array[0], array[1])
    else:
        dynamicList = [array[0], max(array[0], array[1])]
        for i in range(2, len(array)):
            dynamicList.append(
                max(dynamicList[i-1], dynamicList[i-2] + array[i]))

        return dynamicList


array = [4, 3, 5, 200, 5, 3]
print(maxSubsetSumNoAdjacent(array))
