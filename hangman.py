import random
import draw

gameWords = ["mac", "windows", "mouse", "keyboard", "desktop", "trackpad", "wifi", "internet"]

word = random.choice(gameWords) # Selects random word from array

gameWordList = [] # turn gameWord into list 

# function to display word hits during game
def displayHits():
    for char in gameWordList:
        if char in guessArray:
            print (char, end='')
        else:
            print ('-', end='')

#  Opening Message
print(f'Let\'s Play Hangman!\nThis word has {len(word)} letters')

# add letters in word in gameWordList
for letter in word:
    gameWordList.append(letter) # break up word in list
    print("-", end="")

lives = 6 # game lives

guessArray = [] # correct letters guessed list

# List of invalid input 
invalid = ['!',',', '@', '#', '$', '%', '^', '&', '*',
'(', ')', ';',':', '?', '+', '=', '`', '~', '|', '\/', '\"']

while lives > 0:   
    userGuess = input("\nEnter letter:")
    if userGuess.isalpha() and userGuess not in invalid:  # Check for numbers/special characters
        if userGuess in gameWordList:
            guessArray += userGuess
            print("Correct")
        else:
            print("Wrong")
            lives -= 1
            print(f"You Have {lives} lives left!")
    else:
        print('No Numbers or Special Characters!') 
    
    draw.drawBody(lives)  # draws stick figure from draw.py 
    
    displayHits()

    winGame = [char if char in guessArray else "-" for char in gameWordList] # guesses 
    
    if winGame == gameWordList:
        break # break out of while loop if user Wins

if lives > 0:
    print(f"\nYou Win! the word was {word}")
else:
    print (f'\nYou Lose, the word was {word}')
