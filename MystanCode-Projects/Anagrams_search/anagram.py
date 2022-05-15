"""
File: anagram.py
Name:王崇銘
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
# Global variable
dictionary = {}


def main():
    """
    contains
    測試1000次，平均 0.0225 sec
    """
    # start = time.time()
    ####################
    read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        s = input("Find anagrams for: ")
        start = time.time()
        if s == EXIT:
            break
        else:
            s_d = search_dictionary(s)
            find_anagrams(s, s_d)
            end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')
    ####################
    # end = time.time()
    # print('----------------------------------')
    # print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, "r") as f:
        for words in f:
            words = words.strip()
            if len(words) not in dictionary:          # 將所有字依"長度"分類，放入dictionary
                dictionary[len(words)] = [words]
            else:
                dictionary[len(words)].append(words)


def search_dictionary(s):                   # 在dictionary中"單字長度一樣"的類別中排除"字母"不一樣的單字
    s_d = []
    for words in dictionary[len(s)]:
        is_in_s = True
        for letter in words:
            if letter not in s:             # 只要有字母不一樣，排除
                is_in_s = False
                break
        if is_in_s:                         # 字母都包含在輸入值內，加入list
            s_d.append(words)
    return s_d


def find_anagrams(s, s_d):
    """
    :param s:str
    :param s_d: list
    :return:str
    """
    print("Searching...")
    anagram = []
    find_anagrams_helper(s, "", "", len(s), anagram, s_d)
    print(len(anagram), "anagram:", anagram)


def find_anagrams_helper(s, arranged_letter_index, current_s, ans_lens, anagram, s_d):
    if len(current_s) == ans_lens:      # basecase：單字長度一樣
        print("Found: "+current_s)
        print("Searching...")
        anagram.append(current_s)
    else:
        for i in range(len(s)):         # 將單字依照index一一排列組合
            if str(i) not in arranged_letter_index:         # 若該位置排列過，跳過不排列
                current_s += s[i]

                # 若排列的單字不再已確定的anagram，且已排列的字母有在s_d中，繼續排列下一個字母
                if current_s not in anagram and has_prefix(current_s, s_d):
                    arranged_letter_index += str(i)
                    find_anagrams_helper(s, arranged_letter_index, current_s, ans_lens, anagram, s_d)
                    arranged_letter_index = arranged_letter_index[:-1]
                current_s = current_s[:-1]


def has_prefix(sub_s, s_d):
    """
    :param sub_s:list
    :param s_d: list
    :return:boolean
    """
    for words in s_d:
        if words.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
