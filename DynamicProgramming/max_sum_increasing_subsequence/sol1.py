def buildSubSequence(currentIdx, array, subSequence):
    answer = []
    while currentIdx is not None:
        answer.append(array[currentIdx])
        currentIdx = subSequence[currentIdx]

    return list(reversed(answer))


def maxSumIncreasingSubsequence(array):
    maxIdx = 0
    subSequence = [None for _ in array]
    dynamicList = [i for i in array]
    for i in range(0, len(dynamicList)):
        for j in range(i+1, len(dynamicList)):
            if dynamicList[j] < dynamicList[i] + array[j] and array[j] > array[i]:
                dynamicList[j] = dynamicList[i] + array[j]
                subSequence[j] = i
        if dynamicList[i] > dynamicList[maxIdx]:
            maxIdx = i
        print(dynamicList)
    return [dynamicList[maxIdx], buildSubSequence(maxIdx, array, subSequence)]
