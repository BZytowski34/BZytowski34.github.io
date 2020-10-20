---
layout: post
title: Mypolygon
---
``` python
import tkinter
pip install swampy
import swampy
from swampy.AmoebaWorld import AmoebaWorld, Amoeba
world = AmoebaWorld(interactive = True)
world.set_end_time('2*math.pi')
world.set_x_t('10*math.cos(t)')
world.set_y_t('10*math.sin(t)')
amoeba= Amoeba()
world.mainloop()


from IPython.display import clear_output
from swampy.TurtleWorld import * ###imports everything from the turtleworld module in the swampy package

world = TurtleWorld() ##creates a TurtleWorld assigned to world
bob = Turtle() ##creates a Turtle assigned to bob
print(bob) ## yields <swampy.TurtleWorld.Turtle object at 0x000001FF80DC2288>
##which is an instance of a turtle as defined in the module,

##functions for movement are fd, bk, lt, rt
##the turle is holding a pen, pu and pd

##draw a square
def do_twice(f,g,h,i):
    f(h,i)
    g(h)
    

def do_four(f,g,h,i):
    do_twice(f,g,h,i)
    do_twice(f,g,h,i)

def square(bob, length):
    pd(bob)
    do_four(fd,lt,bob,length)
    do_four(fd,lt,bob,length)

for i in range(4):
    fd(bob,100)
    lt(bob)

square(bob,100)


##Exercises
#1) see above
#2)see above
#3)
def polyline(t, length, n, angle):
    """draws multiple line segments. t is a turle. angle is the degree of the turn
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, length, n):
    """draws an n sided polygon whose exterior angles add up to 360 degrees
    """
    angle = 360.0/n
    polyline(t, length, n, angle)
#4)
def arc(t,r,angle):
    """Calculates the arc length of a segment of a circle, then breaks
    the circumference of the circle into n arc segments and calls 
    polyline with its calculations to draw the arc segment. t is a turtle.
    """
    arc_length = 2*math.pi*r*abs(angle)/360
    n = int(arc_length/4)+1
    step_length = arc_length/n
    step_angle = int(angle)/n
    lt(t,step_angle/2)
    polyline(t,step_length,step_angle,n)
    rt(t,step_angle/2)

def circle(t, r):
    """draws a circle of radius r
    """
    arc(t,r,360)



#Exercise 4.2
def petal(t,r,angle):
    for i in range(2):
        arc(t,r,angle)
        lt(t,r,180-angle)

def flower(t,n,r,angle):
    for i in range(n):
        petal(t,r,angle)
        lt(t,r,360.0/n)

def move(t,length):
    pu(t)
    fd(t,length)
    pd(t)

bob.delay = .01
move(bob, -100)
flower(bob,7,60.0,60.0)

move(bob, 100)
flower(bob, 10, 40.0,80.0)

move(bob, 100)
flower(bob, 20, 40.0, 140.0)

die(bob)

def triangle(t, r, angle):
    lt(t, 180-angle)
    fd(t, r)

def pie(t,n,r,angle):
    n= 360/angle
    for i in range(n):
        triangle(t,r,angle)
        lt(t, 180-angle)

wait_for_user()
```
