"""
Docstring for 02_conditions.02_solution
    > problem : 
        > movie tickets are priced based on age : $12 for adults (18 and over) , $8 for children . 
        > everyone gets a $2 discount on wednesday
"""

age = int(input("Enter your age :"))
day = "wednesday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    price = price - 2
    
print("Ticket price for you is $",price)