def isValidSubsequence(array, sequence):
    # Write your code here.
    # O(n) time O(1) space
    seqIdx = 0
    arrIdx = 0
    while seqIdx < len(sequence) and arrIdx < len(array):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)


print(isValidSubsequence([2, 5, 235, 657, 234, 346,
      23432, 4545, 7, 457, 45, 7, 456, ], [7, 7]))
