"""
4️⃣ Daily Transaction Limit

Create DailyLimitExceededError.
Allow maximum withdrawal of ₹10,000 per day.

class DailyLimitExceededError(Exception):
    pass

daily_limit = 10000
withdraw_amount = 0
balance = 15000

try:
    amount = float(input("Enter Withdrawer Amount"))
    if amount + withdraw_amount > daily_limit:
        raise DailyLimitExceededError("Withdraw Limits Exceeded")
    
    balance -= amount
    withdraw_amount += amount
    print("Withdraw sucessfully")
except DailyLimitExceededError as e:
    print("Transaction Failed ",e)  
finally:
    print("Transaction done...")
"""

"""
5️⃣ Student Marks Validation

Create InvalidMarksError.
Raise it if marks entered are less than 0 or greater than 100.


class InvalidMarksError(Exception):
    pass

try:
    marks = int(input("Enter Marks :"))
    if (marks <=0 or marks >100):
        raise InvalidMarksError("Enter Mark between 0 and 100")
    print("done..")
    
except InvalidMarksError as e:
    print("error", e)
"""

"""
6️⃣ E-Commerce Stock System

Create OutOfStockError.
Raise it if ordered quantity exceeds available stock.


count = 10

try:
    quantity = int(input("Enter Quatity to buy :"))
    
    if quantity > count:
        raise Exception("order quantity exceeds available stock")
    
    count -= quantity
    print(f"Thank For Buying {quantity} piece")
    
except Exception as e:
    print("Error" ,e)
    
"""