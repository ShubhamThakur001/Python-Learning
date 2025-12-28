"""
Docstring for 02_conditions.03_solution
    Problem : Assign a letter grade based on a student's score 
        > A [90-100]
        > B [80-89]
        > C [70-79]
        > D [60-69]
        > F [below 60] 
"""

score = int(input("Enter marks below 100 : "))

if(score>100 or score < 0):
    print("Please Enter Below 100")
else:
    if(score >= 90):
        print("Grade : A")
    elif (score >= 80):
        print("Grade : B")
    elif (score >= 70):
        print("Grade : C")
    elif (score >= 60):
        print("Grade : D")
    else :
        print("Grade : F")
    