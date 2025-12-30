"""
Docstring for 04_functions.02_solution
    Program to calculate area and circumference of circle


import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    
    return area,circumference

area , circumference = circle_stats(4)

print("Area" , area , "Circumderence" ,circumference)
"""

"""
Default Value
"""

def greet(name="User"):
    print("Hello , "   + name +   "!")

greet("Shubham")
greet()