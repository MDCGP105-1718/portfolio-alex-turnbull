from random import randint

numberToGuess = randint(0,50)
notGuessed = True
numberOfGuesses = 0

while notGuessed:
    userGuess = int(input("Guess a number between 0-50:  "))
    if userGuess > numberToGuess:
        print("Too High! Try again.")
        numberOfGuesses += 1
    elif userGuess < numberToGuess:
        print("Too Low! Try again.")
        numberOfGuesses += 1
    elif userGuess == numberToGuess:
        numberOfGuesses += 1
        notGuessed = False

print("You got it!")



