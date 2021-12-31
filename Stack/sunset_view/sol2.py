def sunsetViews(buildings, direction):
    # Write your code here.
    # O(n)time O(n)
    # using highest variable
    output = []
    highest = -1
    if direction == "EAST":
        for i in range(0, len(buildings)):
            if buildings[len(buildings) - i - 1] > highest:
                output.insert(0, len(buildings) - i - 1)
                highest = buildings[len(buildings) - i - 1]
    elif direction == "WEST":
        for i in range(0, len(buildings)):
            if buildings[i] > highest:
                output.append(i)
                highest = buildings[i]
    return output
