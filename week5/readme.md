TODO: Reflect on what you learned this week and what is still unclear.

From pandas:
I quite liked the jupyter UI, its a lot more user friendly due to the cells
numpy.ndarray - occurs when the list you're including does not contain a number

python ../course/week5/tests.py

   
Previous code for week 5 exercise:
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
 