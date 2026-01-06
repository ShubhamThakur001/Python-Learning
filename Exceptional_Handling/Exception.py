"""
Docstring for Exceptional_Handling.Exception
"""

# try:
#     Numerator= float(input("Enter a Numerator :"))
#     Demerator = float(input("Enter a Demerator :"))
#     print(Numerator/Demerator)

# except ZeroDivisionError:
#     print("cant divide by zero")
# except ValueError:
#     print("Invaild input")
# else:
#     print("Calculation done!")
# finally:
#     print("Program ended")
    
try:
    num = 10/0
    print(num)
except Exception as e:
    print("Error",e)