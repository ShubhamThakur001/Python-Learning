"""
Docstring for 02_conditions.06_solution
    Problem : determine if a year is a leap year.(leap years are divisible by 4, but not by 100 unless also divisible by 400)
            
"""

year = int(input("Enter year : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 4 !=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")