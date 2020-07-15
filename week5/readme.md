TODO: Reflect on what you learned this week and what is still unclear.

From pandas:
I quite liked the jupyter UI, its a lot more user friendly due to the cells
numpy.ndarray - occurs when the list you're including does not contain a number

python ../course/week5/tests.py

Exercises:
These exercises were okay to complete once I understoof what I was trying to do 

    Notes:
    ** edits the dictionary

    I'm still stuck on wordy_pyramid, I keep on getting the api_key message when I run the test, I removed it and it worked. Unsure if this is the correct thing to do. Same issue with another exercise, I had to remove guard in apply_rules to make it word, guard is not used within that function, only outside of it.

    The fractals was interesting, did a bit of reading on how they work with the angles and movement of the drawing. I slowed down the speed so I could see how it worked.

    Only test I'm failing is the first countdown, but the numbers don't match up. Other's have noted the same issue.

python ../course/new_exercise_getter.py   




Previous code:
    odd_length = []
        even_length = []

        minlength = 3
        maxlength = 21  # needs to be 21 to include the 20 character long words

        for i in range(minlength, maxlength):
            source_with_length = source.format(length=i)
            req = requests.get(source_with_length)
            wordstring = str(req.content)
            if int(i) % 2 == 0:
                even_output = wordstring.split("'")
                even_length.append(even_output[1])
            else:
                odd_output = wordstring.split("'")
                odd_length.append(odd_output[1])

        even_length.reverse()
        pyramid.extend(odd_length)
        pyramid.extend(even_length)
        return pyramid
 