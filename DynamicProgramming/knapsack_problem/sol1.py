# O(nc) time O(nc) space
def knapsackProblem(items, capacity):
    knapsackValue = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]
        for c in range(1, capacity + 1):
            if c < currentWeight:
                knapsackValue[i][c] = knapsackValue[i - 1][c]
            else:
                knapsackValue[i][c] = max(
                    knapsackValue[i - 1][c],
                    knapsackValue[i - 1][c - currentWeight] + currentValue,
                )
    print(knapsackValue[-1][-1])
    return [knapsackValue[-1][-1], getItems(knapsackValue, items)]


def getItems(knapsack, items):
    sequence = []
    i = len(knapsack) - 1
    c = len(knapsack[0]) - 1
    while i > 0:
        if knapsack[i][c] == knapsack[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))


# [value, weights]
items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10
print(knapsackProblem(items, capacity))
