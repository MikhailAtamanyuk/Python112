from math import pi

def rmb(a, b):
    return (a*b)/2

def squ(a):
    return a**2

def trap(a, b, h):
    return 0.5*(a+b)*h

def circle(a):
    return pi*a**2

def func(figure_type, **kwargs):
    if figure_type == "rhombus":
        return rmb(kwargs["d1"], kwargs["d2"])
    elif figure_type == "square":
        return squ(kwargs["a"])
    elif figure_type == "trapezoid":
        return trap(kwargs["a"], kwargs["b"], kwargs["h"])
    elif figure_type == "circle":
        return circle(kwargs["r"])
    elif figure_type == "unknown":
        return "invalid data"

print(func(figure_type="rhombus", d1=10, d2=8))
print(func(figure_type="square", a=5))
print(func(figure_type="trapezoid", a=12, b=3, h=6))
print(func(figure_type="circle", r=18))
print(func(figure_type="unknown", a=1, b=2, c=3))