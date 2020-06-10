"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

#I think this will print the string contained in the list some_words
for word in some_words:
    print(word) #this printed the words from the list in a column, each word from the list is assigned to'word'

#I think this will also print the string contained in the list some_words, x is the index of the string
for x in some_words:
    print(x) #this also printed the words from the list in a column, the function assigns each word to 'x'

#I think it will print the string some_words
print(some_words) #prints the string some_words in square brackets and in a row

#I think this will print the phrase 'some_words contains more than 3 words' if the string contains more than 3 words, which it does
if len(some_words) > 3: 
    print('some_words contains more than 3 words') #it printed 'some_words contains more than 3 words' since there are more than 3 words in the string

#I think this will print out a namedtuple () in round brackets with information about my computer: system, node, release, version, machine, and processor. 
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #prints the following computer details: (system='Darwin', node='17kchaoui17', release='19.0.0', version='Darwin Kernel Version 19.0.0: Thu Oct 17 16:17:15 PDT 2019; root:xnu-6153.41.3~29/RELEASE_X86_64', machine='x86_64', processor='i386')

usefulFunction()
