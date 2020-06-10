TODO: Reflect on what you learned this week and what is still unclear.

Remember to open 'me' folder before testing the code using python ../course/week2/tests.py

Notes:
    ascii is American Standard Code for Information Interchange
    shout() draws from the function above
    '!' adds a punctuation mark to the end of a printed phrase
    " " adds a space
    Upper() = uppercase letters
    == operator compares the value or equality of two objects
    tuple: serquence that is ordered and uses ()

Exercise 2:
    Experienced a "Map object is not subscruptable" error which occured on the 28th line. 

Exercise 3:
    - append() adds a single item to the exisitng list
    - can use count or i (i, j, k used as loop variables)
    - experienced difficulty with variables -> decided to restart and this solved the issue with errors

    loop 6
        struggled converting a block into a triangle, but it made sense to think about it as the row number is equal to the number of columns in the row
        i was able to get it printing the correct format of numbers but did not get a green tick, looking for a minor error
    loop 7
        5 rows and 9 columns therefore max option is col = row+4 - test to identify spaces first
            if c>r+4 -> bottom left trapezium - almost there
            if c<r+4 -> top right triangle x
            if c<r-4 -> rectangle x
            if c>r-4 -> one * x
            if c>4-r -> top left triangle x
            if c<4-r -> bottom right trapezium - almost there

        combine two conditions, using and leads to a rectangle, but using or forms the triangle, identifies which are relevant and 



        had to do a bit of googling but found out how to make a range of numbers only include odd numbers e.g (1,10,2)
