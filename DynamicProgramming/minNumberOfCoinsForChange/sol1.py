def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    minList = [float("inf") for _ in range(n+1)]
    minList[0] = 0
    for denom in denoms:
        for j in range(1, n+1):
            if denom <= j:
                minList[j] = min(minList[j], minList[j-denom]+1)
    return minList[n] if minList[n] != float("inf") else -1
