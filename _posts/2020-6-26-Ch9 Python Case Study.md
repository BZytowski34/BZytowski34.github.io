---
layout: post
title: Ch9_Case_Study
---
```python
fin = open('words.txt')
print(fin)

fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)


def big_words(file):
    fin = open('words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        if len(word) >= 20:
            print(word)

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
        return True


def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True

def uses_all(word, string):
    for letter in string:
        if letter not in word:
            return False
    return True
"""can also be written as:
def uses_all(word,string):
    uses_only(string, word)"""

def cartalk1(word):
    i = 0
    count = 0
    while i < len(word) -1:
        if word[i] == word[i+1]:
            count = count +1
            if count == 3:
                return True
            i = i+2
        else:
            i = i+1
            count = 0

def find_cartalk1():
    fin = open('words.txt')
    line = fin.readline()
    for line in fin:
        word = line.strip()
        if cartalk1(word) == True:
            print(word)

def has_palindrome(i, start, len):
    """returns true if the integer i, when written as a string,
    contains a palindrome with length (len), starting at index (start)"""
    s = str(i)[start:start+len]
    return s[::-1] == s


def check(i):
    """Checks whter the integer (i) has the properties described
    in the puzzler"""
    return(has_palindrome(i,2,4) and
            has_palindrome(i+1,1,5) and
            has_palindrome(i+2,1,4) and
            has_palindrome(i+3, 0, 6))

def check_all():
    i = 100000
    while i <= 999996:
        if check(i):
            print i
        i = i+1

def str_fill(i,len):
    return str(i).zfill(len)

def are_reversed(i, j):
    return str_fill(i,2) == str_fill(j,2)[::-1]
"""start at string length, end at position 0,
move with the step -1 (one step backward)"""

def num_instances(diff, flag = False):
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter,mother) or are_reversed(daughter, mother+1):
            count = count +1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter +1
    return count

def check_diffs():
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n>0:
            print(diff, n)
        diff = diff +1
```
