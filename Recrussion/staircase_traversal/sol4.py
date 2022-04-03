# n: heights, k: number of allow steps
# O(n) time, O(n) space recursive stack height
# sliding windoe approach
def staircaseTraversal(height, maxSteps):
    current_number_of_ways = 0
    ways_to_top = [1]
    for current_height in range(1, height + 1):
        start_window = current_height - maxSteps
        end_window = current_height - 1
        if start_window > 0:
            current_number_of_ways -= ways_to_top[start_window - 1]
        current_number_of_ways += ways_to_top[end_window]
        ways_to_top.append(current_number_of_ways)

    return ways_to_top[height]
