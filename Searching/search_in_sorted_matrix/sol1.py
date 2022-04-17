# O(n+m) time | O(1) space
def searchInSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while col >= 0 and row < len(matrix):
        if target > matrix[row][col]:
            row += 1
        elif target < matrix[row][col]:
            col -= 1
        else:
            return [row, col]
    return [-1, -1]
