"""
Docstring for 02_conditions.01_solution
    if age < 13 print child
    if age between 13 to 19 print teenager
    if age between 20 to 59 print adult
    if age 60+ print senior
    
"""
user_age = int(input("Provide me an age: "))

if user_age < 13:
    print("Child")
elif user_age < 20:
    print("Teenager")
elif user_age < 60:
    print("Adult")
else:
    print("Senior")
    

