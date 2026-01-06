"""
 1️⃣ Age Verification System

    Create a custom exception UnderAgeError.
    Raise it if the user age is below 18 and handle it gracefully.

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter Your Age :"))
    if age < 18:
        raise InvalidAgeError("Age Must be 18+")
    print("done...")
except (InvalidAgeError,ValueError) as e:
    print("Error" , e)
"""

"""
    2️⃣ Password Strength Checker

    Create WeakPasswordError.
    Raise it when the password is less than 8 characters or contains no digit.


def validate_password(password):
    if len(password) < 8:
        raise WeakPasswordError("Min 8 chars required")
    if not any(c.isdigit() for c in password):
        raise WeakPasswordError("At least 1 digit required")

try:
    validate_password(input("Enter password: "))
    print("Password accepted")
except WeakPasswordError as e:
    print("Validation failed:", e)

"""


"""

    3️⃣ Simple ATM Withdrawal

    Create InsufficientBalanceError.
    Raise it if withdrawal amount is greater than account balance.

class InsufficientBalanceError(Exception):
    pass

balance = 5000
withdraw = 6000

try:
    if withdraw > balance:
        raise InsufficientBalanceError("Insufficient Balance")
    balance -= withdraw
    print("withdraw sucessfully")
except InsufficientBalanceError as e:
    print("Error ",e)
"""