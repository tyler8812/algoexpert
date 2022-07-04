# O(n) time | O(n) space
# ASCII a: 97 z:122
def caesarCipherEncryptor(string, key):
    key = key % 26
    new_string = []
    for letter in string:
        print(letter)
        print(ord(letter) + key)
        print((ord(letter) + key) % 122 + 97)
        new_ascii = ord(letter) + key
        if new_ascii > 122:
            new_string.append(chr(new_ascii % 122 + 96))
        else:
            new_string.append(chr(ord(letter) + key))
    print(new_string)
    return "".join(new_string)


test = "ayz"
print(caesarCipherEncryptor(test, 2))
