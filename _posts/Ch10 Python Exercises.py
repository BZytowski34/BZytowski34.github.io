def nested_sum(t):
    diff = 0
    i = 0
    for i in range(len(t)):
        diff += sum(t[i])
        i += 1
    return diff

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(t):
    caps = []
    for i in t:
        caps.append(capitalize_all(i))
    return caps

capitalize_nested([['hello','there'],['buddy']])



def cumulative(t):
    s = t.copy()
    for i in range(1,len(s)): """I am unsure why there is an error here"""
        s[i] += s[i-1]
    return s

def middle(t):
    s = t.copy()
    y = s.pop(len(s)-1)
    x = s.pop(0)
    return s

def chop(t):
    t.pop(0)
    t.pop(len(t)-1)
"""modifies a list by removing the first and last indexes 
and returns None. Must print the list to see the modified list"""
t = ['a','b','c','d','e']

def is_sorted(t):
    letter = 0
    while letter < len(t):
        x = t[letter]
        y = t[letter+1]
        if(x < y or x is y):
            letter += 1
            return True
        else:
            letter += 1
            return False

is_sorted(['a','b'])

def is_anagram(t,l):
    if(is_sorted(t) == False):
        i = 0
        new_t = []
        print(new_t)
        while i < len(t):
            new_t += t[i]
            i += 1
        new_t.sort()
        print(new_t)
    if(is_sorted(l) == False):
        i = 0
        new_l  = []
        print(new_l)
        while i < len(l):
            new_l += l[i]
            i += 1
        new_l.sort()
        print(new_l)
    if(t == l or new_t == new_l):
        return True
    else:
        return False

is_anagram('hello','olleh')

"""sort is a method, not a function, remember this"""

def has_duplicates(t):
    i = 0
    while i < len(t):
        new_list = t[:i] + t[i+1:]
        if(t[i] in new_list):
            return True
        else:
            i+=1
    #print(t)
    return False

has_duplicates('hello')

import random
def birthdays():
    year = random.randint(0,99)
    month = random.randint(1,12)
    if((year + 1900) %4 == 0 and month == 2):
        day = random.randint(0,29)
    elif(month == 2):
        day = random.randint(1,28)
    if(month%2==0 and month != 2 and month < 7):
        day = random.randint(1,30)
    elif(month%2 != 0 and month < 8):
        day = random.randint(1,31)
    elif(month%2 == 0 and month>7):
        day = random.randint(1,31)
    elif(month%2!= 0 and month > 7):
        day = random.randint(1,30)
    day = str(day)
    month = str(month)
    year = str(year)
    birthday = month + '/'+ day + '/'+year
    print(birthday)
    
def same_birthday_odds():
    i = 0
    while i < 23:
        birthday_list = ['']
        birthday_list.append(birthdays())
        i +=1
    has_duplicates(birthday_list)
"""would need to make a for loop with 1000 iterations and find the probability"""
same_birthday_odds()


def remove_duplicates(t):
    i = 0
    while i < len(t):
        new_list = t[:i] + t[i+1:]
        if(t[i] in new_list):
            del(t[i])
            if(t[i] not in new_list):
                i+=1
        else:
            i +=1
    print(t)

remove_duplicates([1,2,3,4,1,2])

def ones(file):
    fin = open(file)
    one_element = []
    text = fin.read()
    text.strip()
    for word in text:
        for letter in word:
            one_element.append(letter)
    print(one_element)



def make_word_list():
    word_list = []
    fin = open("words.txt")
    line = fin.readline()
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

from bisect import bisect_left

def in_bisect(word_list, word):
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in ['alien', 'allen']:
        print(word, 'in list', in_bisect(word_list, word))
