"""
Docstring for 02_conditions.04_solution
    Determine if a fruit is ripe , overripe , or unripe based on it's color 
        > (e.g : Banana:Green - unripe , yellow - ripe , brown - overripe)
"""

fruit = input("Enter fruit name : ")
color = input("Enter fruit color : ")

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("ripe")
    elif color == "Brown":
        print("Overripe")
else:
    print("Invalid fruit")