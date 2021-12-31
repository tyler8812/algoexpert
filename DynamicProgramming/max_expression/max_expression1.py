def maximizeExpression(array):
    # Write your code here.
    # 	O(n^4)time O(1)sapce
    import math
    if len(array) < 4:
        return 0

    maxmumValue = -math.inf

    for a in range(len(array)):
        aValue = array[a]
        for b in range(a+1, len(array)):
            bValue = array[b]
            for c in range(b+1, len(array)):
                cValue = array[c]
                for d in range(c+1, len(array)):
                    dValue = array[d]
                    tempValue = aValue - bValue + cValue - dValue
                    # print(tempValue, maxmumValue)
                    maxmumValue = max(tempValue, maxmumValue)

                    # print(maxmunValue)

    return maxmumValue


print(maximizeExpression([[3, 6, 1, -3, 2, 7]]))
