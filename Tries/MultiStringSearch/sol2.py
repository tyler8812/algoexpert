# O(b^2 + ns) time | O(b^2 + n) space
# n: length of the small strings
# b: length of big string
# s: length of the biggest small string


def multiStringSearch(bigString, smallStrings):
    suffix_trie = ModifiedSuffixTrie(bigString)
    return [suffix_trie.contains(string) for string in smallStrings]


class ModifiedSuffixTrie:
    def __init__(self, string) -> None:
        self.root = {}
        self.populate_modified_suffix_trie(string)
        print(self.root)

    def populate_modified_suffix_trie(self, string):
        for i in range(len(string)):
            self.insert_substring(i, string)

    def insert_substring(self, idx, string):
        node = self.root
        for j in range(idx, len(string)):
            char = string[j]
            if char not in node:
                node[char] = {}
            node = node[char]

    def contains(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return True


test = {
    "bigString": "this is a big string",
    "smallStrings": ["this", "yo", "is", "a", "bigger", "string", "kappa"],
}
suffix_trie = ModifiedSuffixTrie(test["bigString"])
