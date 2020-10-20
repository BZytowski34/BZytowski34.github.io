"""Write a compare function that reutnrs 1
if x>y, 0 if x==y, and -1 if x<y."""

def compare(x,y):
    if x>y:
        return 1
    if x==y:
        return 0
    if x<y:
        return -1

def ask_compare():
    prompt_x = "Input value for x. \n"
    x = int(input(prompt_x))
    prompt_y = "Input value for y. \n"
    y = int(input(prompt_y))
    print(compare(x,y))

ask_compare()
import math
def distance(x1,x2,y1,y2):
    dx = x2-x1
    dy = y2-y1
    d_squared = dx**2 + dy**2
    d = math.sqrt(d_squared)
    return d

def area(d):
    area = math.pi * (d**2)
    return area


def circle_area(xc,xp, yc, yp):
    return area(distance(xc,xp, yc, yp))
    ###area of a circle when give a point on the circle


def hypotenuse(leg1, leg2):
    hypotenuse_squared = leg1**2 + leg2**2
    print(hypotenuse_squared)
    hypotenuse = math.sqrt(hypotenuse_squared)
    return hypotenuse

def is_between(x,y,z):
    if x<=y and y<=z:
        return True
    else:
        return False


is_between(1,2,3)


def ack(m,n):
    if m == 0:
        return n+1
    elif n<0 or m<0:
        print('Ack is defined for integer n,m>=0')
    elif n==0 and m > 0:
        m_recursion = ack(m-1,1)
        return m_recursion
    elif m>0 and n>0:
        n_recursion = ack(m,n-1)
        last_recursion = ack(m-1,n_recursion)
        return last_recursion


def is_power(a,b):
    if a%b ==0 and (a/b)%b==0:
        return True
    else:
        return False

def gcd(a,b):
    if b ==0:
        return a
    r = a%b
    if r == 0:
        return b
    elif gcd(b,r) == 0:
        return r
    else:
        return gcd(b,r)
