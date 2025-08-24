def is_valid_path(board, path, words):
    """

    :param board: an input
    :param path: a tuple of coordinates that shows the place of the word in a board
    :param words: a list of words
    :return: the word of the given path
    """
    lst = []
    for i in range(len(path)):
        if path[i][0] < 0 or path[i][0] >= len(board) or path[i][1] < 0 or path[i][1] >= len(board[0]):
            return None
    for x in range(len(path) - 1):
        if abs(path[x + 1][0] - path[x][0]) > 1 or abs(path[x + 1][1] - path[x][1] > 1) > 1:
            return None
    for j in range(len(path)):
        lst.append(board[path[j][0]][path[j][1]])
    chosen_word = ''.join(str(i) for i in lst)
    for word in words:
        if chosen_word == word:
            return chosen_word


def find_length_n_paths(n, board, words):
    """

    :param n: the length of the path
    :param board: the board with the letter
    :param words: a list of words
    :return: all paths with the length of n that returns a given word
    """
    paths = []
    for word in words:
        new_paths = find_path(board, word)
        for path in new_paths:
            path2 = {c for c in path}
            if len(path2) == len(path) == n:
                word2 = [board[i][j] for i, j in path]
                if word == "".join(word2):
                    paths.append(path)
    return paths


DIRECTIONS = {(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)}


def find_path_helper(board, word, coordinate, path, paths):
    """

    :param board: the board with the letters
    :param word: a given word
    :param coordinate: the coordinates of the word
    :param path: the path with the coordinates of the word
    :param paths: a list of paths
    :return: a boolean value
    """
    i, j = coordinate
    if len(word) == 0:
        if path not in paths:
            paths.append(path)
        return True
    if not 0 <= i < len(board) or not 0 <= j < len(board[i]):
        return False
    letters = board[i][j]
    if word[0:len(letters)] != letters:
        return False
    for d in DIRECTIONS:
        if find_path_helper(board, word[len(letters):], (i + d[0], j + d[1]), path + [(i, j)], paths):
            continue

    return False


def find_path(board, word):
    """

    :param board: an input
    :param word: a given word
    :return: the paths of a word in the board
    """
    paths = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            letters = board[i][j]
            if word[0:len(letters)] == board[i][j]:
                path = []
                find_path_helper(board, word, (i, j), path, paths)
    return paths


def find_length_n_words(n, board, words):
    """

    :param n: the length of a word
    :param board: an input
    :param words: a list of words
    :return: the paths that lead to the word in the board
    """
    paths = []
    for word in words:
        if len(word) != n:
            continue
        new_paths = find_path(board, word)
        for path in new_paths:
            path2 = {c for c in path}
            if len(path2) == len(path):
                word2 = [board[i][j] for i, j in path]
                if word == "".join(word2):
                    paths.append(path)
    return paths


def max_score_paths(board, words):
    """

    :param board: a input
    :param words: a list of words
    :return: the path with the maximum length
    """
    max_paths = []
    for word in words:
        paths = find_path(board, word)
        if paths:
            max_path = []
            for path in paths:
                path2 = {coord for coord in path}
                if len(path) == len(path2):
                    word2 = [board[i][j] for i, j in path]
                    if word == "".join(word2):
                        if len(path) > len(max_path):
                            max_path = path
            max_paths.append(max_path)
    return max_paths


def load_words_dict(file):
    milon = open(file)
    lines = set(line.strip() for line in milon.readlines())
    milon.close()
    return lines

