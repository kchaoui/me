TODO: Reflect on what you learned this week and what is still unclear.

python ../course/week3/tests.py


Exception -> needs a capital E

range(10) -> range(0,10) is a range object

list(range(10)) -> [0,1,2,3,4,5,6,7,8,9] 0 to 9 and not 1 to 10

### Exercise 1:
    stubborn_asker: 
        my issues with this is I wanted it to print Perfect! when the number was guessed correctly but this caused an error and it only worked when I deleted it
        might ask Ben for help on this one
            Edit: got it working

     not_number_rejector:
        found the function isinstance(object, type) which returns true if the object is of the correct type, I don't think I know how to use this correctly
        another funciton .isdigit worked well, I like the way the .is... functions work - will use again
    super_asker:
        this one was okay once I figured out how to incorporate the other function into the super_asker
        I fiddled around with the printing function to make sure that it outputted the correct phrases
        need to learn how to use Try and Exception

### Exercise 2:
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

### Exercise 3:
    Syntax Notes:  \n = new line
    
    I've figured out how to incorporate the upper and lower bound inputs into the game and it works. 
        Now I need to add the non integer value paramter into it, most likely using the non_number_rejector from exercise 1
        Also need to create a rule that will not accept if the lower>upper bound

        Edit: main issues was the text that was printing was coming from the not_number_rejector rather than the guessing game, needed to change "pick a number" to message so it references the game's print code

### Exercise 4:
    I liked this exercise, it was a lot more straight forward than I thought, replicates some of the iterative methods I have used in previous courses but on Excel
        * binary_search(low, high, actual_number) => three integers that need to be used in the code for the function to work
        * 'break' stop a while loop - Needed this when python input an infinite list of 100s
        * += x adds x onto the variable

    The issues I had with this code is that everytime I tested it, it would only guess 50 and try one time. The debugger didn't come up with anything because there was nothing technically wrong with the code, it just was not working correctly.
        edit: I looked through some examples and the position of the 'break' is important, I shifted it forward so it only stops the function once it is correct

    I tried to complete this code using the guessed = False function but I could not get it to work properly, mainly due to the code taking too many tries to get the correct answer. I will probably look into this further later on. This is why i used the high>low as part of the while function.

### Homework:
Looking through everyone's code, there are some are that easier to understand especially for someone who has very basic coding knowledge. 
        Most codes used a combination of 4-i and 4+1, the reasoning behind this is pretty straight forward but a code like FlimEden's is a bit more complex and I would need to do a bit of googling to understand it. Some of the shorter codes are more challenging to understand as the functions are less 'spoon fed' while reading
    
     