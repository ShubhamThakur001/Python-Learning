"""

"""
import random
class BankAccount:
    DAILY_LIMIT = 5000  
    
    def __init__(self,name,account_no,pin,balance=0):
        self.name=name
        self.account_no=account_no
        self.__pin = pin
        self.__balance = balance
        self.transaction_history = []
        self.daily_withdrawn = 0
      
    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid Amount!")
            return
        
        self.__balance = self.__balance + amount
        self.transaction_history.append(f"Deposit ₹: {amount} ")
        return f"Deposit ₹{amount} sucessfully"
    
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Amount")
            return
        
        if amount > self.__balance:
            print("Insufficant Balance")
            return
        
        if amount + self.daily_withdrawn > BankAccount.DAILY_LIMIT:
            print("Daily limits is over")
            return
        
        self.__balance=self.__balance - amount
        self.transaction_history.append(f"Withdraw ₹: {amount}")
        self.daily_withdrawn += amount
        return f"Withdraw ₹{amount} sucessfully"
    
    def verify_pin(self,pin):
        return self.__pin == pin
    
    def account_info(self):
        print(f"Account number :",self.account_no)
        print(f"Name : ",self.name)
        print(f"Balance ₹: ",self.__balance)
        
    def ministate_bank(self):
        if not self.transaction_history:
            print("No Transaction yet")
            return
        for x in self.transaction_history:
            print('-' , x)
            
  
def account_number_generator():
    account_number = random.randrange(1000,9999)
    if account_number in accounts:
        return account_number_generator()
    return account_number
          
accounts = {}


def create_account():
    account_number = account_number_generator()
    name = input("What is your name : ")
    pin = int(input("Enter Pin [4-Digits]"))
    amount = int(input("Enter initial amount:"))
    
    accounts[account_number] = BankAccount(name,account_number,pin,amount)
    print(f"{name} , your account number is {account_number}")
    return
    

def login():
    
    account_number = int(input("Enter your account number : "))
    pin = int(input("Enter your pin"))
    account = accounts.get(account_number)
    if account and account.verify_pin(pin):
        print(f"\n login sucessfully Welcome , {account.name}")
        
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Logout")

            choice = input("Enter Choice : ")

            if choice == '1':
                print("Current Balance ",account.get_balance())
            elif choice == '2':
                amount = int(input("Enter Amount to Deposit: "))
                print(account.deposit(amount))
            elif choice == '3':
                amount = int(input("Enter Amount to Withdraw: "))
                print(account.withdraw(amount))
            elif choice == '4':
                print(account.ministate_bank())
            elif choice == '5':
                print("Thank you ")
                break
            else:
                print("Enter Valid Choice")
    else:
        print("Invalid account number or pin")
        
while True:
    print("\n=== SHUBHAM BANK SYSTEM ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        if not accounts:
            print("No accounts found. Please create an account first.")
        else:
            login()

    elif choice == "3":
        print("Thank you for using Shubham Bank!")
        break

    else:
        print("Invalid choice")