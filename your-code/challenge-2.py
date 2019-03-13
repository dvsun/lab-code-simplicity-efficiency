"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

"""I import the libraries at the beginning"""
"""I changed the name of all variables in order to asign them a significant name"""
"""I delete non useful code"""

import sys
from random import choice

"""I write the list of the elements outside the function"""

var_list =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           '0','1','2','3','4','5','6','7','8','9']

def RandomStringGenerator(length):
    counter = 0
    string = ''
    while counter<length:
        string += choice(var_list)
        counter += 1
    return string

def BatchStringGenerator(n_gen, a_gen, b_gen):
    list_string = []
    for i in range(n_gen):
        if a_gen <= b_gen:
            length_gen = choice(range(a_gen, b_gen+1))
        else:
            sys.exit('Incorrect min and max string lengths. Try again.')
        list_string.append(RandomStringGenerator(length_gen))
    return list_string

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))

