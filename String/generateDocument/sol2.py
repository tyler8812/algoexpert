# O(m * (n + m)) time | O(1) space
# n is the number of characters, m is the characters of document
def generateDocument(characters, document):
    for character in document:
        document_frequency = count_frequency(character, document)
        characters_frequency = count_frequency(character, characters)
        if characters_frequency < document_frequency:
            return False
    return True


def count_frequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

print(generateDocument(characters, document))
