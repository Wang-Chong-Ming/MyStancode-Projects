"""
File: anagram_extension.py
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
    測試1000次，平均 0.008 sec
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
            find_anagrams(s)
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
            if len(words) not in dictionary:        # 將所有字依"長度"分類，放入dictionary
                dictionary[len(words)] = [words]
            else:
                dictionary[len(words)].append(words)


def find_anagrams(s):
    anagrams = []
    print("Search...")
    for words in dictionary[len(s)]:
        is_in_s = True
        for letter in words:        # 只要有字母不一樣，排除
            if letter not in s:
                is_in_s = False
                break
        if is_in_s:
            # 將輸入的單字變成list，再重新排列
            s_list = list(s)
            s_list.sort()

            # 將所有長度/字母一樣的單字變成list，再重新排列
            words_list = list(words)
            words_list.sort()

            # 若兩個list相等，即找到anagram
            if s_list == words_list:
                print("Found: "+words)
                anagrams.append(words)
                print("Search...")
    print(len(anagrams), "anagram:", anagrams)


if __name__ == '__main__':
    main()


