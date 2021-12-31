def numbersInPi(pi, numbers):
    # 	add to hash table
    # 倒著回來
    numbersTables = {number: True for number in numbers}
    cache = {}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, numbersTables, cache, i)
    return -1 if cache[0] == float("inf") else cache[0]


def getMinSpaces(pi, numbersTables, cache, index):
    if index == len(pi):
        return -1
    if index in cache:
        return cache[index]
    minSpaces = float("inf")
    for i in range(index, len(pi)):
        # 		找前綴是否在hash table
        prefix = pi[index : i + 1]
        if prefix in numbersTables:
            minSpaceInSuffix = getMinSpaces(pi, numbersTables, cache, i + 1)
            # 			更新minSpace，藉由之前的prefix和當前的比較
            # 			3 14 5 6三個。 31 45 6 兩個
            minSpaces = min(minSpaces, minSpaceInSuffix + 1)

    cache[index] = minSpaces
    return cache[index]
