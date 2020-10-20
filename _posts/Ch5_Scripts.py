#5.3

import math
def check_fermat(a,b,c,n):
    if n > 2:
        if (a**n) + (b**n) == (c**n):
            print('Holy smokes, Fermat was wrong!')
        else:
            print("No, that doesn't work.")
    else:
        print("Yes, that works")

def fermat_query():
    for i in range(4):
        if i == 0:
            prompt = "Input value for a.\n"
        if i == 1:
            prompt = "Input value for b. \n"
        if i == 2:
            prompt = "Input value for c. \n"
        if i == 3:
            prompt = "Input value for n. \n"
        value_i_str = input(prompt)
        value_i_int = int(value_i_str)
        inputs = [value_i_str]
        if i == 4:
            return
    check_fermat(inputs[0], inputs[1], inputs[2], inputs[3])
    prompt_a = "Input value for a.\n"
    value_a = input(prompt_a)
    prompt_b = "Input value for b.\n"
    value_b = input(prompt_b)
    prompt_c = "Input value for c.\n"
    value_c = input(prompt_c)
    prompt_n = "Input value for n.\n"
    value_n = input(prompt_n)
    a = int(value_a)
    b = int(value_b)
    c = int(value_c)
    n = int(value_n)
    check_fermat(a,b,c,n)



    #5.4
def is_triangle(a,b,c):
    if int(a+b) < int(c) or int(a+c) < int(b) or int(c+b) < int(a):
        print("No.")
    elif int(a+b) == int(c) or int(b+c) == int(a) or int(c+a) == int(b):
        print("No.")
    else:
        print("No.")


is_triangle(1,2,2)

def ask_is_triangle():
    prompt_a = "Input value for a. \n"
    leg_a = int(input(prompt_a))
    prompt_b = "Input value for b. \n"
    leg_b = int(input(prompt_b))
    prompt_c = "Input value for c. \n"
    leg_c = int(input(prompt_c))
    is_triangle(leg_a, leg_b, leg_c)

#5.4
from swampy import TurtleWorld
from swampy.TurtleWorld import *


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)


def koch(t,length):
    if length < 3:
        fd(t, length)
        return
    n = length/3.0
    koch(t, n)
    lt(t, 60)
    koch(t, n)
    rt(t, 120)
    koch(t, n)
    lt(t, 60)
    koch(t, n)

def snowflake(t, length):
    for i in range(3):
        koch(t, length)
        rt(t, 120)


world = TurtleWorld()
bob = Turtle()
bob.delay = .01

bob.x = -150
bob.y = 50
bob.redraw()
snowflake(bob, 300)

world.mainloop()

def equilateral_triangle(t, length):
    fd(t, length)
    lt(t, 120)
    fd(t, length)
    lt(t, 120)
    fd(t, length)
    lt(t, 120)
