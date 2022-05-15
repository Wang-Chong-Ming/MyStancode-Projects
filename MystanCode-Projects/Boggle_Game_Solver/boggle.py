"""
File: boggle.py
Name:王崇銘
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = {}


def main():
    """
	TODO:
	"""
    read_dictionary()
    ####################
    matrix = set_matrix()       # 輸入英文字母

    # 測試用
    # matrix = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]

    start = time.time()

    find_words(matrix)      # 開始搜尋單字

    end = time.time()
    ####################
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def set_matrix():
    matrix = []
    for i in range(4):
        correct_input = False
        while not correct_input:
            letter = input(str(i + 1) + " rows of letters: ")

            # 判斷input是否符合格式
            if len(letter) == 7 and letter[1] == letter[3] == letter[5] == " " and letter[0].isalpha() \
                    and letter[2].isalpha() and letter[4].isalpha() and letter[6].isalpha():
                letter = letter.lower()
                letter = letter.split()
                matrix.append(letter)
                correct_input = True
            else:
                print("illegal input")
    return matrix


def find_words(matrix):
    total_words = []
    i = j = 0
    find_words_helper(matrix, "", total_words, [], i, j)
    print("There are " + str(len(total_words)) + " words in total.")


def find_words_helper(matrix, current_s, total_words, current_index, current_i, current_j):

    # Base Case
    if len(current_s) >= 4 and current_s not in total_words:
        if current_s in dictionary[current_s[0]]:
            print("Found:" + current_s)
            total_words.append(current_s)
            find_words_helper(matrix, current_s, total_words, current_index, current_i, current_j)
    else:
        # Recursive
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(current_index) == 0:     # 判斷是否第一個字母
                    current_s += matrix[i][j]
                    if has_prefix(current_s):
                        current_index.append((i, j))
                        find_words_helper(matrix, current_s, total_words, current_index, i, j)
                        current_index.pop()
                    current_s = current_s[:-1]
                else:
                    if (i, j) not in current_index and current_i - 1 <= i <= current_i + 1 and current_j - 1 <= j <= \
                            current_j + 1:      # 判斷排列的字母是否在周圍，且排列已使用過的字母
                        current_s += matrix[i][j]
                        if has_prefix(current_s):
                            current_index.append((i, j))
                            find_words_helper(matrix, current_s, total_words, current_index, i, j)
                            current_index.pop()
                        current_s = current_s[:-1]


def read_dictionary():
    """
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
    with open(FILE, "r") as f:
        for words in f:
            words = words.strip()
            if words[0] not in dictionary:  # 將所有字依"第一個字母"分類，放入dictionary
                dictionary[words[0]] = [words]
            else:
                dictionary[words[0]].append(words)


def has_prefix(sub_s):
    """
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
    for words in dictionary[sub_s[0]]:
        if words.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
