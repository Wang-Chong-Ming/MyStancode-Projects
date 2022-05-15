"""
File: hangman.py
Name:王崇銘
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    1.設定答案
    2.用"-"隱藏的答案
    3.設定猜的次數
    4.檢查輸入的格式是否正確
    5.判斷是否猜中
        5.1 沒猜中，次數扣1，並判斷是否次數歸零，若歸零則死亡，反之回到第4步
        5.2 若猜中，將猜中的字母顯示，並判斷是否全猜中，若尚未猜完，則回到第4步，反之勝利。
    """
    answer = random_word()
    dashed_answer = dashed(answer)
    print("The words looks like: " + dashed_answer)
    print("You have " + str(N_TURNS) + " guess left.")
    b = N_TURNS
    while True:
        a = input_and_check()
        if answer.find(a) == -1:    # 判斷是否猜中
            print("There is no " + a + "'s in the word.")
            b -= 1          # 猜錯,次數減1
            if b == 0:      # 若無次數,死亡
                print("You are completely hung : ( ")
                print("The word was: REFUND ")
                break
            else:
                print("The words looks like: " + dashed_answer)
                print("You have " + str(b) + " guess left.")
        else:
            print("You are correct!")  # 猜對
            dashed_answer = change_dashed_word(a, answer, dashed_answer)    # 將"-"換成字母
            if dashed_answer in answer:     # 若全換成字母,成功
                print("You win!")
                print("The word was: " + answer)
                break
            else:
                print("The words looks like: " + dashed_answer)     # 還沒全對,顯示目前結果
                print("You have " + str(b) + " guess left.")    # 還沒全對,顯示目前次數


def input_and_check():  # 檢查輸入是否正確
    while True:
        a = input("You guess: ")
        a = a.upper()
        if not a.isalpha() or len(a) != 1:  # 判斷a是否為數字
            print("illegal format")
        else:
            return a


def change_dashed_word(a, answer, dashed_answer):
    i = ""
    for j in range(len(answer)):
        if a == answer[j]:  # 判斷猜的字母在第幾個位置
            i += a  # 在該位置串入該字母
        else:
            i += dashed_answer[j]   # 其餘位置串入目前的答案(可能為字母或"-")
    return i


def dashed(answer):     # 將答案用"-"# 隱藏
    a = ""
    for i in range(len(answer)):
        a += "-"
    return a


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
