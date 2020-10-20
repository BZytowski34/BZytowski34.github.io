---
layout: post
title: Ch12_Scripts
---
```python
def sumall(*n):
    """n is a tuple, or any number of arguments"""
    total = 0
    for i in n:
        total += i
    return total


n = (2,3,5,6,8)

from random import *
def sort_by_length(words):
    t= []
    for word in words:
        t.append((len(word), random(), word))
    
    t.sort(reverse= True)
    res = []
    for length, _, word in t:
        res.append(word)
    return res

words = ['John', 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']
t = sort_by_length(words)
for x in t:
    print(x)


def make_histogram(string):
    hist = {}
    for x in string:
        hist[x] = hist.get(x,0) + 1
    return hist

def read_file(file_name):
    return open(file_name).read()

def most_frequent(string):
    hist = make_histogram(string)
    frequencies = []
    for x, val in hist.items():
        frequencies.append((x,val))
    
    frequencies.sort(reverse = True)
    res = []
    for x,val in frequencies:
        res.append(x)
    return res


string = read_file('words.txt')
t = most_frequent(string)
for x in t:
    print(x)



def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    for v in d.values():
        if len(v) > 1:
            print(len(v),v)

def print_anagram_sets_in_order(d):
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v),v))
    t.sort()
    for v in t:
        print(v)

def filter_length(d,n):
    res = {}
    for word, anagrams in d.items():
        if len(word) ==n:
            res[word] = anagrams
    return res

d = all_anagrams('words.txt')
print_anagram_sets_in_order(d)

eight_letters = filter_length(d, 8)
print_anagram_sets_in_order(eight_letters)
```
