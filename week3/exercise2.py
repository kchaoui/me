"""Week 3, Exercise 2.

An example of how a guessing game might be written.
"""


import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = input("Enter an upper bound: ") #asks for an upper bound
    print("OK then, a number between 0 and {} ?".format(upperBound)) #{} is the placeholder for the upperbound that is inputted
    upperBound = int(upperBound) #converts the input into an integer for python to read

    actualNumber = random.randint(0, upperBound) #finds a random number between 0 and upperbound

    guessed = False 

    while not guessed:
        guessedNumber = int(input("Guess a number: ")) #asks for a guess
        print("You guessed {},".format(guessedNumber),) #prints the guess
        if guessedNumber == actualNumber: 
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
