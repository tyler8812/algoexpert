def isValidSubsequence(array, sequence):
    # Write your code here.
    # O(n) time O(1) space
    sequenceIdx = 0
    for value in array:
        if sequenceIdx == len(sequence):
            break
        if value == sequence[sequenceIdx]:
            sequenceIdx += 1
    return sequenceIdx == len(sequence)
