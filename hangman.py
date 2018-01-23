import random
import re


wordsArray = ["mac", "windows", "mouse", "keyboard", "desktop"]

word = (random.choice(wordsArray))

lives = int(5)

print ('Lets play Hangman!\nHint: Computer terms')
print ("Lives: %d" %(lives))
wordArr = list(word)
print wordArr
for index in word:
    print ("-"),

userLetter = (raw_input('\nChoose a letter: '))
