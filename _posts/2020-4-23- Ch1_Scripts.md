---
layout: post
title: Ch1_Scripts.py
---

s = 'hi'
print(s[1])
print(len(s))
print(s + 'there')

pi= 3.14
text = 'the value of pi is ' + str(pi)
print(text)

raw = r'\nthis and that'
print(raw)

print(len(raw))

#multi = """It was the best of times. 
#It was the worst of times."""
#print(multi)

#divisor = 6//5
#print(divisor)


for i in range(len(multi)-1):
    if multi[i] == " ":
       print("The " + str(i) + " index is white space")

#print(multi[1:4]) ##prints t w
#print(multi[:]) ##prints all of multi
#print(multi[1:100]) ##prints all of multi because the index > len(multi) so it truncates to len(multi)
#print(multi[:4]) ##prints It w
#print(multi[1:]) ##omits the 0th index and prints the entire string

s = 'hello'
print(s[-4]) #prints e, the 4th from the end
print(s[-1]) #prints l, the frist from the end
print(s[:-3]) #prints he, goes up to but does not include the last 3 chars
print(s[-3:]) #prints llo, starts with the 3rd char from the end and prints until the end

text = ("%d little pigs come out,
" or I'll %s, and I'll %s,"
" and I'll blow your house %s down." 
% (3, 'huff', 'puff', 'house'))
print(text)

