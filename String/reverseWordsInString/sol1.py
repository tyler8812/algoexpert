# O(n) time | O(n) space
def reverseWordsInString(string):
    start_of_word = 0
    word_list = []
    for i in range(len(string)):
        character = string[i]
        if character == " ":
            print(start_of_word, i)
            print(string[start_of_word:i])
            word_list.append(string[start_of_word:i])
            start_of_word = i + 1

    word_list.append(string[start_of_word : len(string)])
    print(word_list)
    reverse_list = []
    for i in range(len(word_list)):
        reverse_list.append(word_list[len(word_list) - i - 1])
    print(reverse_list)

    return " ".join(reverse_list)


test = "AlgoExpert is the best!"
print(reverseWordsInString(test))
