# Program: HANGMAN written by Nhan Thi Thanh Le, 18th Nov 2020
import random
words = ['python', 'java', 'kotlin', 'javascript']
n = random.randint(0, len(words)-1)
word = words[n]
l = len(word)
# Print information of the guessed word
print("HANGMAN")
print('-'*l)
# Set start value
win = False
times = 0
guessed = []
checkword = ['-' for i in range(l)]
# Write main program - using while
while not win and times<8 :
    m = input("Input the letter: > ")
    # The letter in word
    if m in word:
        # The letter wasn't be guessed before
        if m not in guessed:
            guessed.append(m)
            for i in range(l):
                if word[i] == m:
                    checkword[i] = m
            for i in checkword:
                print(i, end='')
            print()
            # The player win
            if checkword.count('-') == 0:
                win = True
                print("You guessed the word!")
                print("You survived!")
        else:
            # The letter is in word but was be guessed
            times += 1
            print("No improvements")
    # The letter is not in word
    elif m not in word:
        times += 1
        print("No such letter in the word")
# Game over!
if not win:
    print("You are hanged!")
