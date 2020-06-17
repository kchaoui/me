TODO: Reflect on what you learned this week and what is still unclear.

Exception -> needs a capital E

range(10) -> range(0,10) is a range object

list(range(10)) -> [0,1,2,3,4,5,6,7,8,9] 0 to 9 and not 1 to 10

Exercise 1:
    stubborn_asker: 
        my issues with this is I wanted it to print Perfect! when the number was guessed correctly but this caused an error and it only worked when I deleted it
        might ask Ben for help on this one

     not_number_rejector:
        found the function isinstance(object, type) which returns true if the object is of the correct type, I don't think I know how to use this correctly
        another funciton .isdigit worked well, I like the way the .is... functions work - will use again
    super_asker:
        this one was okay once I figured out how to incorporate the other function into the super_asker
        I filled around with the printing function to make sure that it outputted the correct phrases
        need to learn how to use Try and Exception

Exercise 2:
    Decided to add comments to the code to talk myself through how it is working
    Steps:
    1. Asks for an upper bound 
        Prints the range
    2. Sources a random number   
    3. Guesses 
        If correct - prints correct and the statement is true
        If too small - prints to try again
        If too big - prints to try again
    4. returns you got it when the answer is correct   
    I'm going to attempt to use those comments to completed ex3

 Exercise 3:
    Syntax Notes:
    \n = new line




    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    lowerBound = input("Enter a lower bound: ")
    print("OK then, a number between {lower} and _ ?".format(lower=lowerBound)
    lowerBound = int(lowerBound)
    upperBound = input("Enter an upper bound: ")
    print("OK then, a number between {lower} and {upper} ?".format(lower=lowerBound, upper=upperBound)
    upperBound = int(upperBound)