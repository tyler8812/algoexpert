# O(ns + bs) time | O(ns) space
# n: length of the small strings
# b: length of big string
# s: length of the biggest small string


def multiStringSearch(bigString, smallStrings):
    trie = Trie()
    for string in smallStrings:
        trie.insert(string)
    contain_string = {}
    for i in range(len(bigString)):
        find_small_string_in_big_string(bigString, i, trie, contain_string)
    return [string in contain_string for string in smallStrings]


def find_small_string_in_big_string(string, start_idx, trie, contain_string):
    node = trie.root
    for i in range(start_idx, len(string)):
        if string[i] not in node:
            break
        node = node[string[i]]
        if trie.end_symbol in node:
            contain_string[node[trie.end_symbol]] = True


class Trie:
    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"

    def insert(self, string):
        node = self.root
        for char in string:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end_symbol] = string
