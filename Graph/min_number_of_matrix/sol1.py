# O(w*h) time | O(w*h) space
# w: width, h: height
def minimumPassesOfMatrix(matrix):
    iter_time = convert_negatives(matrix)
    return iter_time - 1 if not contains_negative(matrix) else -1


def convert_negatives(matrix):
    next_current_positive = get_positive_position(matrix)
    iter_time = 0
    while len(next_current_positive) > 0:
        current_positive = next_current_positive
        print(current_positive)
        next_current_positive = []
        while len(current_positive) > 0:
            # In python, poping elements from the start of a list is an O(n) time.
            # To make this an O(1) time, we could use deque object.
            # But now we just use stack to compare with stack.
            current_row, current_col = current_positive.pop(0)
            neighbors = get_neighbors(matrix, current_row, current_col)
            for neighbor in neighbors:
                neighbor_row, neighbor_col = neighbor
                if matrix[neighbor_row][neighbor_col] < 0:
                    matrix[neighbor_row][neighbor_col] *= -1
                    next_current_positive.append((neighbor_row, neighbor_col))
        iter_time += 1
    return iter_time


def get_positive_position(matrix):
    positive_pos = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                positive_pos.append((row, col))
    return positive_pos


def get_neighbors(matrix, row, col):
    max_row = len(matrix)
    max_col = len(matrix[row])
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < max_row - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < max_col - 1:
        neighbors.append((row, col + 1))
    return neighbors


def contains_negative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False


test = [[0, -1, -3, 2, 0], [1, -2, -5, -1, -3], [3, 0, 0, -4, -1]]
print(minimumPassesOfMatrix(test))
