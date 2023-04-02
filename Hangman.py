import random
import string

from Words import words

def getvalidword(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word =getvalidword(words)
    word= word.upper()
    wordletters =set(word)
    alphabet = set(string.ascii_uppercase)
    usedletters = set()
    print(wordletters)
    #wordletters[0].upper
    while len(wordletters) >0:

        print("you have guessed ", " ".join(usedletters))

        wordlist = [letter if letter in usedletters else '_' for letter in word]
        print("current word ", " ".join(wordlist))
        userletter=input("guess letter").upper()
        if userletter in alphabet - usedletters:
            usedletters.add(userletter)
            if userletter in wordletters:
                wordletters.remove(userletter)
        elif userletter in usedletters:
            print("you have already used that letter")
        else:
            print("invalid character")

hangman()