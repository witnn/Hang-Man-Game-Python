# The simple HangMan game on python, Written by Baris Kivanc "witnn"

from hmPics import pictures as pic;
import random as rd;
import time

nativeList = ["man", "hang", "rope", "tree", "fire", "punishment", "escape",
            "arm", "leg", "head", "body", "stick"]

class wordListObj():
    def __init__(self, list):
        self.wordList = list
wl = wordListObj(nativeList)

def menu():
    print("\n"+"-" * 11 + "\nHangManGame\n"+"-" * 11)
    while True:
        print("1 - Play game\n2 - Options")
        choice = str(input("\nWhat do you want : "))
        if choice == "1":
            if len(wl.wordList) > 0:
                game()
            else:
                print("Word list is empty, you should add words or reset the list.\n")
        elif choice == "2":
            options()
        else:
            print("Wrong entry")

def game():
    wordSelected = rd.choice(wl.wordList)
    word = wordSelected.lower()
    letters = list(word)
    index = []
    for i in range(len(letters)):
        index.append("-")

    health = 6
    while True:
        if health == 6:
            print(pic[6])
        if health == 5:
            print(pic[5])
        if health == 4:
            print(pic[4])
        if health == 3:
            print(pic[3])
        if health == 2:
            print(pic[2])
        if health == 1:
            print(pic[1])

        for i in range(len(index)):
            print(index[i], end="")
        print("")

        character = str(input("Enter a letter : "))

        failtime = 0
        for i in range(len(letters)):
            if character == letters[i]:
                index[i] = letters[i]

            else:
                failtime += 1

        if failtime == len(letters):
            print("\n Fail!")
            health -= 1

        remSpace = 0
        for i in index:
            if i == "-":
                remSpace += 1
        if remSpace == 0:
            print("\nThe word was : "+word)
            win()

        if health == 0:
            lose()
            break

def lose():
    print(pic[0])
    print("You lose, man is dead")
    time.sleep(1)
    menu()

def win():
    print("You win")
    time.sleep(1)
    menu()

def options():
    print("\n"+"-" * 8 + "\nOptions\n"+"-" * 8)
    while True:
        print("1 - Add word to word list\n2 - Clear the word list\n3 - Use native word list\n4 - Back to menu")
        choice = str(input("\nWhat do you want : "))
        if choice == "1":
            newChar = str(input("Add new word : "))
            wl.wordList.append(newChar)
            print(f"new word added. word list contains {len(wl.wordList)} words! \n")
        elif choice == "2":
            wl.wordList = []
            print(f"Word list cleared, it contains {len(wl.wordList)} words now \n")
        elif choice == "3":
            wl.wordList = nativeList
            print(f"Reverted factory settings, word list contains {len(wl.wordList)} words now \n")
        elif choice == "4":
            menu()
        else:
            print("Wrong entry\n")

menu()