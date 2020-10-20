a = 4
x = 3
y=(x+(a/x))/2

while x!=y:
    x=y
    y=(x+a/x)/2
    print(y)




def square_root(a):
    x=a
    y=(x+a/x)/2
    epsilon = .00000000001
    while abs(y-x)>= epsilon:
        x=y
        y=(x+a/x)/2
        return y
"""Using Newton's Method and the Epsilon-Delta approximation"""
def difference(x,y):
    difference = x-y
    if difference <0:
        return -difference
    else:
        return difference

import math

def test_square_root(a):
    for i in range(a):
        function = square_root(a)
        sq_rt = math.sqrt(a)
        """num_white_spaces_1 = len(square_root(9))-len(square_root(a))+1
        num_white_spaces_2 = len(math.sqrt(9)) - len(math.sqrt(a))+1
        num_white_spaces_3 = len(difference(square_root(2),math.sqrt(2))) - len(difference(square_root(a),math.sqrt(a)))"""
        print(a, '' ,function(a) ,'' , sq_rt(a) ,'', difference(function(a),sq_rt(a)))

        """Cant get it to print the way I want it to but they are the correct numbers"""

def eval_loop():
    while True:
        number = input('> ')
        if number == 'done':
            break
        evaluation = eval(number)
        print(evaluation)
    return evaluation

def factorial(n):
    if not isinstance(n,int):
        print('Factorial is only defined for integers')
        return None
    elif n<0:
        print('Facorial is not defines for negative integers.')
        return None
    elif n== 0:
        return 1
    else:
        return n*factorial(n-1)

def estimate_pi():
    k = 0
    total = 0
    factor = 2*math.sqrt(2)/9801
    while True:
        num = factorial(4*k)*(1103+26390*k)
        den = factorial(k)**4*396**(4*k)
        term = factor*num/den
        if abs(term) < 1e-15:
            break
        k = k+1
        total += term
    return 1/total

print(estimate_pi())

"""Prints a string in reverse. String is a string."""
def backward(string):
    index = 0
    while index < len(string):
        letter = string[-index-1]
        print(letter)
        index = index + 1

def quack():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == 'Q' or letter == 'O':
            print(letter + 'u' + suffix)
        else:
            print(letter + suffix)


def find(word,letter, index):
    if index >= len(word):
        return 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

word = 'banana'
index = word.count('a')
print(index)

"""A string slice can take a third index that specifies the
'step size.' The number of spaces between successive characters.
A step size of 2 means every other character; 3 means every third, etc.
fruit = 'banana'
fruit[0:5:2]
'bnn'
A step of size -1 goes through the word backwards, so the slice 
[::-1] generates a reverse string"""
def is_palindrome(word):
    if word == word[::-1]:
        return True

"""rotates the word by the given number of spaces. a is an int"""
def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    c = ord(letter) - start
    i = (c+n)%26 + start
    return chr(i)

def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter,n)
    return res
        
