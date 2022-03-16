# O(row * col * size * size) time | O(1) space
def maximumSumSubmatrix(matrix, size):
    row_length = len(matrix)
    col_length = len(matrix[0])
    maximum = float("-inf")
    for row in range(row_length - size + 1):
        for col in range(col_length - size + 1):

            current_value = 0
            for i in range(row, row + size):
                for j in range(col, col + size):
                    current_value += matrix[i][j]
            maximum = max(maximum, current_value)
    return maximum
