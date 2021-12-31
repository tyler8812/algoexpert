def moveElementToEnd(array, toMove):
    # Write your code here.
    # O(n) time	O(n) space
    notToMove = []
    count = 0
    for i in range(len(array)):
        if array[i] != toMove:
            notToMove.append(array[i])
        else:
            count += 1
    while count > 0:
        notToMove.append(toMove)
        count -= 1

    return notToMove
