# time: O(wh) | space: O(wh)
# w: width, h: height
def removeIslands(matrix):
    one_connected_to_border = [[False for col in matrix[0]] for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            row_is_border = row == 0 or row == len(matrix) - 1
            col_is_border = col == 0 or col == len(matrix[row]) - 1
            is_border = row_is_border or col_is_border
            if not is_border:
                continue
            if matrix[row][col] == 1:
                find_ones_connected_to_border(matrix, row, col, one_connected_to_border)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if one_connected_to_border[row][col]:
                continue
            matrix[row][col] = 0

    return matrix


def find_ones_connected_to_border(
    matrix, start_row, start_col, one_connected_to_border
):
    stack = [(start_row, start_col)]

    while len(stack):
        current_pos = stack.pop()
        current_row, current_col = current_pos
        visited = one_connected_to_border[current_row][current_col]
        if visited:
            continue
        one_connected_to_border[current_row][current_col] = True

        neighbors = get_neighbors(matrix, current_row, current_col)
        for neighbor in neighbors:
            row, col = neighbor
            if matrix[row][col] == 1:
                stack.append((row, col))


def get_neighbors(matrix, row, col):
    neighbors = []
    num_rows = len(matrix)
    num_cols = len(matrix[row])
    # up neighbor
    if row > 0:
        neighbors.append((row - 1, col))
    # down neighbors
    if row < num_rows - 1:
        neighbors.append((row + 1, col))
    # right neighbors
    if col < num_cols - 1:
        neighbors.append((row, col + 1))
    # left neighbors
    if col > 0:
        neighbors.append((row, col - 1))
    return neighbors


test = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]

print(removeIslands(test))
