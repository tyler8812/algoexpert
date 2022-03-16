def boggleBoard(board, words):
    final_words = {}
    trie = Trie()
    for word in words:
        trie.add(word)
    visited = [[False for _ in row] for row in board]
    for row in range(len(board)):
        for col in range(len(board[row])):
            traverse_all_possible_words(
                row, col, board, trie.root, final_words, visited
            )

    return list(final_words.keys())


# using dfs
def traverse_all_possible_words(row, col, board, trie_node, final_words, visited):
    letter = board[row][col]
    if letter not in trie_node:
        return
    if visited[row][col]:
        return
    visited[row][col] = True
    trie_node = trie_node[letter]
    # end of letter
    if "*" in trie_node:
        final_words[trie_node["*"]] = True
    current_neighbors = get_neighbors(board, row, col)
    for neighbor in current_neighbors:
        traverse_all_possible_words(
            neighbor[0], neighbor[1], board, trie_node, final_words, visited
        )
    visited = False


def get_neighbors(board, row, col):
    neighbors = []
    if row > 0:
        # middle top
        neighbors.append((row - 1, col))
        # left top
        if col > 0:
            neighbors.append((row - 1, col - 1))
        # right top
        if col < len(board[0]) - 1:
            neighbors.append((row - 1, col + 1))
    # left middle
    if col > 0:
        neighbors.append((row, col - 1))
    # right middle
    if col < len(board[0]) - 1:
        neighbors.append((row, col + 1))
    if row < len(board) - 1:
        # middle down
        neighbors.append((row + 1, col))
        # left down
        if col > 0:
            neighbors.append((row + 1, col - 1))
        # right down
        if col < len(board[0]) - 1:
            neighbors.append((row + 1, col + 1))

    return neighbors


class Trie:
    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = word
