---
layout: post
title: Ch11_Scripts
---
```python

eng2sp = dict()
eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one':'uno', 'two':'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])


def words_dictionary(file):
    """Write a function that creates a dictionary
    of the words in words.txt with the words as
    the keys, the values do not matter for this
    example."""
    fin = open(file)
    dictionary = dict()
    i = 0
    while i <= len(dictionary):
        word = fin.readline()
        dictionary[word.strip().lower] = i
        i += 1
    return dictionary


def histogram(string):
    count = dict()
    for i in string:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

def print_hist(h):
    h_list = sorted(h.keys())
    for i in h_list:
        print(i, h[i])

h = histogram('parrot')
print_hist(h)



def reverse_lookup(d,v):
    keys = []
    for k in d:
        if d[k] == v:
           keys.append(k)
    return keys 
    #raise ValueError('value does not appear in the dictionary')

k = reverse_lookup(h,'r')
"""This is an error, the reverse lookup function 
takes in an index, not a dictionary value"""
k = reverse_lookup(h, 1)
print(k)

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

inverse = invert_dict(h)
print(inverse)


def has_duplicates(t):
    return len(set(t))<len(t)

t= ['this','is','a','list']
has_duplicates(t)

def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter,n)
    return res

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

def rotate_pairs(dictionary, word):
    rotated_pairs = []
    for i in range(1,14):
        rotated_word = rotate_word(word, i)
        if rotated_word in dictionary:
            pair = word + ',' + rotated_word
            rotated_pairs.append(pair)
    return rotate_pairs


dictionary = words_dictionary('words.txt')
for word in dictionary:
    rotate_pairs(dictionary, word)
```
