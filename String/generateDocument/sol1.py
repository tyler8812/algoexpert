# O(n+m) time | O(c) space
# n is the number of characters, m is the characters of document
# c is the number of unique number of characters
def generateDocument(characters, document):
    dictionary = {}
    for char in characters:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    for char in document:
        if char in dictionary:
            if dictionary[char] == 1:
                del dictionary[char]
            else:
                dictionary[char] -= 1
        else:
            return False
    return True


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

print(generateDocument(characters, document))
