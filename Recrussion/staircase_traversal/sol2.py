# n: heights, k: number of allow steps
# O(n * k) time, O(n) space recursive stack height
def staircaseTraversal(height, maxSteps):
    memory = {0: 1, 1: 1}
    return number_of_ways_to_top(height, maxSteps, memory)


def number_of_ways_to_top(height, maxSteps, memory):
    print(memory)
    if height in memory:
        return memory[height]

    number_of_ways = 0

    for step in range(1, min(height, maxSteps) + 1):
        number_of_ways += number_of_ways_to_top(height - step, maxSteps, memory)
    memory[height] = number_of_ways
    return number_of_ways


height = 4
maxStep = 2

staircaseTraversal(4, 2)
