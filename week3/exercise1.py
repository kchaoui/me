# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """
    #copy what the range function does using a different loop function

    number_1=[]
    x=start #x has a starting value
    while x<stop: 
        print(x)
        number_1.append(x)
        x=x+step
    return number_1


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """

    number_2=[]
    for i in range(start,stop,step):
        number_2.append(i)
    return number_2


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    
    number_3=[]
    for i in range(start,stop,2): #include 2 in the range func so step size always = 2
        number_3.append(i)
    return number_3


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """
    
    number_4 = False

    while number_4 == False:
        guess = int(input("Pick a number: "))
        if low < guess < high:
            number_4 = True
            print ("Perfect!")
        elif guess< low or guess>high:
            print ("Not quite, pick another number")
    return int(guess)


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """

    number_5 = False

    while number_5 == False:
        ask = str(input("Pick a number: "))
        if ask.isdigit():
            print("great, it's a number!")
            return int(ask)
        else:
            print ("Try again, that's not a number")
    

    

def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """

    number_6 = False

    while number_6 == False:
        guess = not_number_rejector("Pick a number: ") #makes the variable guess run with the not_number_rejection function
        if low < guess < high:
            number_6 = True
            print ("That is correct!")
            return guess
        elif guess< low or guess>high:
            print ("But it is not within range")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
