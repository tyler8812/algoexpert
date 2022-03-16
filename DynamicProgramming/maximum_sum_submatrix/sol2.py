# O(row * col) time | O(row * col) space


def maximumSumSubmatrix(matrix, size):
    sum_matrix = create_sum_matrix(matrix)
    maximum = float("-inf")
    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[0])):
            total = sum_matrix[row][col]
            minus_top = row - size >= 0
            minus_left = col - size >= 0
            if minus_top:
                total -= sum_matrix[row - size][col]
            if minus_left:
                total -= sum_matrix[row][col - size]
            if minus_top and minus_left:
                total += sum_matrix[row - size][col - size]
            maximum = max(maximum, total)
    return maximum


def create_sum_matrix(matrix):
    sums = [[0 for _ in matrix[0]] for _ in matrix]
    sums[0][0] = matrix[0][0]
    # fill the first col
    for idx in range(1, len(matrix[0])):
        sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]
    # fill the first row
    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]
    # finish filling the sum_matrix
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            sums[row][col] = (
                matrix[row][col]
                + sums[row - 1][col]
                + sums[row][col - 1]
                - sums[row - 1][col - 1]
            )
    return sums
