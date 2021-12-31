def spiralTraverse(array):
    # using direction for right, down, left, up
    answer = []
    n = len(array)
    m = len(array[0])
    row = 0
    col = 0
    count = n * m
    direction = 0
    last = 0
    while len(answer) < count:
        if direction == 0:
            direction = 1
            answer, row, col = right(row, col, answer, array, n, m, last)
            row += 1
        elif direction == 1:
            direction = 2
            answer, row, col = down(row, col, answer, array, n, m, last)
            col -= 1
        elif direction == 2:
            direction = 3
            answer, row, col = left(row, col, answer, array, n, m, last)
            row -= 1
            last += 1
        elif direction == 3:
            direction = 0
            answer, row, col = up(row, col, answer, array, n, m, last)
            col += 1
        else:
            print("got error")
    return answer


def right(row, col, answer, array, n, m, last):
    print("right", row, col)
    temp = -1
    for i in range(col, m - last):
        answer.append(array[row][i])
        temp = i
    col = temp
    return answer, row, col


def left(row, col, answer, array, n, m, last):
    print("left", row, col)
    temp = -1
    for i in range(col, last-1, -1):
        answer.append(array[row][i])
        temp = i
    col = temp
    return answer, row, col


def down(row, col, answer, array, n, m, last):
    print("down", row, col)
    temp = -1
    for i in range(row, n - last):
        answer.append(array[i][col])
        temp = i
    row = temp
    return answer, row, col


def up(row, col, answer, array, n, m, last):
    print("up", row, col)
    temp = -1
    for i in range(row, last-1, -1):
        answer.append(array[i][col])
        temp = i
    row = temp
    return answer, row, col
