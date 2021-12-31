def spiralTraverse(array):
    # Write your code here.
    # O(n) time O(n) space n is the total number of element in array
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # 		right
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])
    # 		down
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])
    # 		left
        for col in reversed(range(startCol, endCol)):
           # 		假如中間只有一行，不要重複算
            if startRow == endRow:
                break
            result.append(array[endRow][col])
    # 		up
        for row in reversed(range(startRow + 1, endRow)):
           # 		假如中間只有一列，不要重複算
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1

    return result
