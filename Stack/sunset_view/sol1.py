def sunsetViews(buildings, direction):
    # Write your code here.
    # O(n^2)time O(n) space
    output = []
    if direction == "EAST":
        for i in range(0, len(buildings)):
            check = 0
            for j in range(i+1, len(buildings)):
                if buildings[i] <= buildings[j]:
                    check = 1
                    break
            if not check:
                output.append(i)

    elif direction == "WEST":
        for i in range(0, len(buildings)):
            check = 0
            for j in range(0, i):
                if buildings[i] <= buildings[j]:
                    check = 1
                    break
            if not check:
                output.append(i)
    return output
