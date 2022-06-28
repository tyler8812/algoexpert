# O(n^2) time | O(1) space
def largestRectangleUnderSkyline(buildings):
    max_area = 0
    for i in range(len(buildings)):
        left_idx = i
        right_idx = i
        while left_idx - 1 >= 0 and buildings[left_idx - 1] >= buildings[i]:
            left_idx -= 1
        while (
            right_idx + 1 <= len(buildings) - 1
            and buildings[right_idx + 1] >= buildings[i]
        ):
            right_idx += 1

        current_area = buildings[i] * (right_idx - left_idx + 1)
        max_area = max(max_area, current_area)
        print(current_area)
    return max_area


test = [1, 3, 3, 2, 4, 1, 5, 3, 2]

print(largestRectangleUnderSkyline(test))
