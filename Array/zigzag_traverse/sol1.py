def zigzagTraverse(array):
    # Write your code here.
    # O(N) time O(N) N is all of the number in array

    # check at first roww first column
    # check at last row last col
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []

    currentRow, currentCol = 0, 0
    goingDown = True

    while not outOfBounds(currentRow, currentCol, height, width):
        result.append(array[currentRow][currentCol])
        if goingDown:
            # 判斷是否在第一col或最後一row
            if currentCol == 0 or currentRow == height:
                goingDown = False
                if currentRow == height:
                    currentCol += 1
                elif currentCol == 0:
                    currentRow += 1
                else:
                    print("will not get inside")
            # 在做斜著往下
            else:
                currentRow += 1
                currentCol -= 1
        else:
            # 到上面或右邊 要把direction往下了
            if currentRow == 0 or currentCol == width:
                goingDown = True
                if currentCol == width:
                    currentRow += 1
                elif currentRow == 0:
                    currentCol += 1
                else:
                    print("will not get inside")
            else:
                currentRow -= 1
                currentCol += 1

    return result


def outOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width
