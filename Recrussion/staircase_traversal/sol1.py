# n: heights, k: number of allow steps
# O(k ^ n) time, O(n) space recursive stack height
def staircaseTraversal(height, maxSteps):
    return number_of_ways_to_top(height, maxSteps)


def number_of_ways_to_top(height, maxSteps):
    if height <= 1:
        return 1

    number_of_ways = 0

    for step in range(1, min(height, maxSteps) + 1):
        number_of_ways += number_of_ways_to_top(height - step, maxSteps)

    return number_of_ways
