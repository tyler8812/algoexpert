def sunsetViews(buildings, direction):
    # Write your code here.
    # O(2n)time O(n) space
    # using stack
    candidate = []

    start = 0 if direction == "EAST" else len(buildings) - 1
    step = 1 if direction == "EAST" else -1

    idx = start
    while idx >= 0 and idx < len(buildings):
        height = buildings[idx]
        while len(candidate) > 0 and buildings[candidate[-1]] <= height:
            candidate.pop()
        candidate.append(idx)

        idx += step
    if direction == "WEST":
        return candidate[::-1]
    return candidate
