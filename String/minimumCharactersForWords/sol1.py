# O(m * n) time | O(c) space
# m: length of words, n: length of word, c: unique characters
def minimumCharactersForWords(words):
    main_map = {}
    result = []
    for word in words:
        temp_map = {}
        for char in word:
            if char not in temp_map:
                temp_map[char] = 1
            else:
                temp_map[char] += 1

            if char not in main_map:
                result.append(char)
                main_map[char] = 1
            else:
                if main_map[char] < temp_map[char]:
                    main_map[char] += 1
                    result.append(char)
        print(temp_map, main_map)
    print(result)
    return result


test = ["this", "that", "did", "deed", "them!", "a"]
minimumCharactersForWords(test)
