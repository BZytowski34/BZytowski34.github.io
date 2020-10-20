---
layout: post
title: Ch3_Scripts
---
```python
##Exercise 3.3 write a function named right_justify that takes
##a string named s as a parameter and prints the string
##with enough leading spaces so that the last letter of
##the string is in column 70 of the display.

s = 'allen'
def right_justify(s):
    length= len(s)
    num_spaces = 70-length
    print(' '*(num_spaces))
    print(s)

#Exercise 3.4 1)Type the example into a script and test it.
#2) Modify do_twice so that it takes two arguments, a function object
#and a value, and  calls the function twice, passing the value as an argument
#3) Write a more general version of print_spam, called print_twice, that takes a string
# as a parameter and prints it twice. 4) Use the modified version of do_twice
#to call print_twice twice, passing 'spam' as an argument.
#5) Define a new function called do_four tha takes a function object and a value
#and calls the function four times, passing the value as a parameter. 
#There should be only two statements in the body of this function


    
#4)
def do_twice(f):
    f()
    f()

def print_twice(s):
    print(s*2)
    


#5)
def do_four(f):
    do_twice(f)
    do_twice(f)


def one_four_one(f,g,h):
    f()
    do_four(g)
    h()

def print_plus():
    print('+'),

def print_dash():
    print('-'),

def print_bar():
    print('|'),

def print_space():
    print(' '),

def print_end():
    print

def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_plus, print_dash)

def print1bar():
    one_four_one(nothing, print_bar, print_space)

def print4bar():
    one_four_one(print_bar, print1bar, print_end)

def print4beam():
    one_four_one(print_plus, print1beam, print_end)

def print_row():
    one_four_one(nothing, print4bar, print4beam)

def print_grid():
    one_four_one(print4beam, print_row, nothing)

print_grid()
```
