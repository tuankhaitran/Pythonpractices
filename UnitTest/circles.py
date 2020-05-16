#Calculate circle area

from math import pi

def circle_area(r):
    if type(r) not in [int,float]:
        raise TypeError("The radius should be integer")
    if r<0:
        raise ValueError("The radius should be positive")
    return pi*(r**2)
