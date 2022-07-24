# create: O(n^2) time | O(n^2) space
# searching: O(m) time | O(1) space
# n string length
# m searching string length
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insert_char_to_dictionary(i, string)
        print(self.root)

    def insert_char_to_dictionary(self, idx, string):
        node = self.root
        for j in range(idx, len(string)):
            if string[j] not in node:
                node[string[j]] = {}
            node = node[string[j]]
        node[self.endSymbol] = True

    def contains(self, string):
        node = self.root
        for char in string:
            if char in node:
                node = node[char]
            else:
                return False
        print(self.endSymbol in node)
        return self.endSymbol in node


test = SuffixTrie("babc")
test.contains("ba")
test.contains("bc")
