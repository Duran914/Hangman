import random
import re
import sys
wordsArray = ["mac", "windows", "mouse", "keyboard", "desktop", "trackpad"]

word = (random.choice(wordsArray))

lives = 5

loss = 0
guesses = ''
wordArr = list(word)

print ('Lets play Hangman!\nHint: Computer terms')
print word
print ("Lives: %d" %(lives))

for char in word:
    print ("-"),

while lives != 0:
    guess = (raw_input('\nChoose a letter: '))
    guesses += guess
    for char in word:
        if char in guesses:
            print char,
        else:
            print ('-'),
        if guess not in word:
            lives -= 1
            print ('Wrong, You have %d lives left' %(lives))
            break
    if guesses == word:
        print ('\nYou Win!')
        sys.exit()
print ('Sorry you lost!, The word was %s' %(word))
