"""
Docstring for 02_conditions.05_solution
    Problem : check if a password is "weak","medium",or "strong".
        > creteria : < 6 chars (weaks)
                     < between [6 to 10] (medium)
                     <  >10 (strong)
"""

password = input("Enter a password : ").strip()
length = len(password)

if(length < 6):
    print("Weak password")
elif(length <= 10):
    print("Medium password")
else:
    print("Strong password")

