# O(n^2) time | O(1) space
def firstNonRepeatingCharacter(string):
    first_non_repeating = None
    for i in range(len(string)):
        repeating = False
        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                repeating = True
                break

        if not repeating:
            return i

    return -1


print(firstNonRepeatingCharacter("faadabcbbebdf"))
