---
layout: post
title: Palindrome
---
```python
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

word = "hockey"

def is_palindrome(word):
    first_letter = first(word)
    middle_letters = middle(word)
    last_letter = last(word)
    if len(word) < 3:
        if first_letter == last_letter:
            return True
        else:
            return False
    else:
        if first_letter != last_letter:
            return False
        elif first_letter == last_letter and len(middle_letters) == 1:
            return True
        elif first_letter == last_letter and len(middle_letters) > 1:
            return is_palindrome(middle_letters)

"""The way I wrote it above is quite long and unnecessary. 
this is more attractive:
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))"""
```
