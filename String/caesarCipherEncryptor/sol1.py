# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    alphabat = "abcdefghijklmnopqrstuvwxyz"
    key = key % 26
    new_string = []
    for letter in string:
        idx = alphabat.index(letter)
        new_string.append(alphabat[(idx + key) % 26])

    return "".join(new_string)
