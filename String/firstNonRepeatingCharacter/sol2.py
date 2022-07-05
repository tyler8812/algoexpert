# O(n) time | O(1) space
# The constant space is because the input string only has lowercase
# our hash table will never have more than 26 characters
def firstNonRepeatingCharacter(string):
    characters = {}
    for char in string:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    for idx in range(len(string)):
        character = string[idx]
        if characters[character] == 1:
            return idx
    return -1
