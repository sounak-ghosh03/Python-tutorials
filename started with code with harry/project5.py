"""
BANK ACCOUNT MANAGEMENT SYSTEM
DATA MEMBERS:
    1.Name of the account holder
    2.Account number
    3.Type of account
    4.Account Balance
METHODS:
    1.To deposit an amount
    2.To withdraw an amount after checking the balance
    3.To display the name and balance
"""


class BankAccount:
    def __init__(self, name, acc_no, acc_type, acc_bal):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.acc_bal = acc_bal

    def deposit(self, amount):
        self.acc_bal += amount
        print(f"₹ {amount} has been deposited in your account")
        print("Balance: ₹",self.acc_bal)

    def withdraw(self, amount):
        if (amount > self.acc_bal):
            print("CANNOT WITHDRAW DUE TO INSUFFICIENT BALANCE")
            print("Balance: ₹",self.acc_bal)
        else:
            self.acc_bal -= amount
            print(f"₹ {amount} has been withdrawn from your account")
            print("Balance: ₹",self.acc_bal)

    def display(self):
        print("Name: ", self.name)
        print("Account Type: ",self.acc_type)
        print("Current Balance: ₹", self.acc_bal)
        

n = input("Enter name of the account holder: ")
num = int(input("Enter the account number: "))
type = input("Enter the type of account: ")
b = int(input("Enter the account balance: "))

obj = BankAccount(n, num, type, b)
while(True):
    task=int(input("Enter 1 to deposit and 2 to withdraw and 0 to end transaction: "))
    if (task==1):
        d = int(input("Enter the amount to be deposited: "))
        obj.deposit(d)
    elif(task==2): 
        w = int(input("Enter the amount to be withdrawn: "))
        obj.withdraw(w)
    else:
        print("\nTransaction Completed THANK YOU!!")
        break
obj.display()