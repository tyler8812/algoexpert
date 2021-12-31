def getNthFib(n, fibTable={1: 0, 2: 1}):
    # Write your code here.
    # 	O(n)time O(n)space
    if n in fibTable:
        return fibTable[n]
    else:
        fibTable[n] = getNthFib(n-1, fibTable) + getNthFib(n-2, fibTable)
        return fibTable[n]
