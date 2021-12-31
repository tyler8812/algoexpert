def getNthFib(n):
    # Write your code here.
    # 	O(n)time O(1)space
    fibTable = [0, 1]
    if n == 1:
        return fibTable[0]
    while(n > 2):
        n = n-1
        temp = fibTable[1]
        fibTable[1] = fibTable[1] + fibTable[0]
        fibTable[0] = temp

    return fibTable[1]
