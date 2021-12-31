def nonConstructibleChange(coins):
    # Write your code here.
    # 	O(nlog(n)) time O(1) space
    minAmount = 0
    coins.sort()

    for coin in coins:
        if coin > minAmount + 1:
            return minAmount + 1

        minAmount += coin

    return minAmount + 1
