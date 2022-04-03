# n: heights, k: number of allow steps
# iteratively
# O(n * k) time, O(n) space
def staircaseTraversal(height, maxSteps):
    ways_to_top = [0 for _ in range(height + 1)]
    ways_to_top[0], ways_to_top[1] = 1, 1

    for current_height in range(2, height + 1):
        step = 1
        while step <= maxSteps and current_height - step >= 0:
            ways_to_top[current_height] += ways_to_top[current_height - step]
            step += 1

    return ways_to_top[height]
