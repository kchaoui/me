"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """


    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = not_number_rejector("Enter a lower bound: ") 

    #need to ensure that upper bound > lower bound, use stubborn_asker for reference
    guess = False 

    while guess == False:
      upperBound = not_number_rejector("Enter an upper bound: ")
      if upperBound > lowerBound:
          guess=True
      else:
          print ("Pick a higher number")
        
    print("OK then, guess a number between {lower} and {upper} ?".format(lower=lowerBound,upper=upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound) 

    guessed = False 

    while not guessed:
        guessedNumber = not_number_rejector("Guess a number: ") 
        print("You guessed {},".format(guessedNumber),) 
        if guessedNumber == actualNumber: 
            print("Finally! You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Terrible guess, {} is too small. Try again and guess another number.".format(guessedNumber))
        else:
            print("Hmmm {} is too big, try again.".format(guessedNumber))
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!







def not_number_rejector(message):
  
    number_5 = False

    while number_5 == False:
        ask = str(input(message)) #pick a number
        if ask.isdigit():
            return int(ask)
        else:
            print ("Try again, that's not a number")




if __name__ == "__main__":
    print(advancedGuessingGame())
