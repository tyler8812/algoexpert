# O(w * n * log(n) + n * w * log(w)) time | O(w * n) space
# w: word numbers, n: longest word length


def groupAnagrams(words):
    if len(words) == 0:
        return []
    # w * n * log(n) time
    sorted_words = ["".join(sorted(w)) for w in words]
    print(sorted_words)
    indices = [i for i in range(len(words))]
    print(indices)
    # n * w * log(w) time
    indices.sort(key=lambda x: sorted_words[x])
    print(indices)
    result = []
    current_group = []
    current_anagram = sorted_words[indices[0]]
    for index in indices:
        word = words[index]
        sorted_word = sorted_words[index]

        if sorted_word == current_anagram:
            current_group.append(word)
            continue

        result.append(current_group)
        current_group = [word]
        current_anagram = sorted_word

    result.append(current_group)
    return result


test = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(test))
