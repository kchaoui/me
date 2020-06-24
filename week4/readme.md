TODO: Reflect on what you learned this week and what is still unclear.

python ../course/week4/tests.py

Exercise 1:
    get_some_details
        - data["results"][0]["name"]["last"]
        this accesses the data, into results then name then last
        - need to follow the sequence of Json files

    wordy_pyramid
        problems: every word was formatted with a b in front e.g. "b'quacksalver'". This b needed to be removed, use the .split ("'")function to split the output into individual parts and select the second part to isolate the word
        
        
        status_code is 200 (means okay)
        status_code is 404 (means error)
        .content pulls the word from the website and makes it a string
        .split = split a string into a list where each word is a list item
        .extent = adds all elements of an iterable list to the end of the list
        .reverse = revereses elemnts of the list





        no of columns
        no of rows
        what type each column is
            boolean
            point
            string
            who recorded the data and why it was recorded (legislative body, organisation), when - the origin of the data source