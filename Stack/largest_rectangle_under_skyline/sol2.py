# O(n) time | O(n) space
def largestRectangleUnderSkyline(buildings):
    stack = []
    max_area = 0
    for idx, height in enumerate(buildings + [0]):

        while len(stack) != 0 and buildings[stack[-1]] >= height:
            current_height = buildings[stack.pop()]
            width = idx if len(stack) == 0 else idx - stack[-1] - 1
            current_area = current_height * (width)
            max_area = max(max_area, current_area)

        stack.append(idx)

    return max_area


test = [1, 3, 3, 2, 4, 1, 5, 3, 2]

print(largestRectangleUnderSkyline(test))
