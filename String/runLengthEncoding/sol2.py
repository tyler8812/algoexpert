def runLengthEncoding(string):
    # Write your code here.
    # 	don't use string because string+= get O(n)
    # O(n) time O(2n) space
    answerChar = []
    length = 1
    for i in range(1, len(string)):
        char = string[i]
        prev = string[i - 1]

        if char != prev or length == 9:
            answerChar.append(str(length))
            answerChar.append(prev)
            length = 0

        length += 1

    answerChar.append(str(length))
    answerChar.append(string[len(string) - 1])

    return ''.join(answerChar)
