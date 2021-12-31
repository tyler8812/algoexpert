def numbersInPi(pi, numbers):
    # O(n^3 + m) time
    # space O(n+m) n: pi stringm m: favorite array
    # 是n+m是因為要有m個hash table和有一個cache紀錄每個index的min number space
    # Write your code here.
    # 	add to hash table
    # 順著過去
    numbersTables = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTables, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces


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
