# Write a Python program to create a class named BankAccount with attributes owner and balance. Implement methods to deposit, withdraw, and check the balance of the account. Also, implement a method to transfer money from one account to another.
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = Owner
        self.balance = Balance
    def deposite(self):
        d_amount = float(input("Enter the amount to deposite: "))
        self.balance = d_amount+self.balance
    def withdraw(self):
        w_amount = float(input("Enter the amount to withdraw:"))
        if w_amount > self.balance:
            print("Not sufficient balance")
        else:
            self.balance = self.balance - w_amount
    def check_balance(self):
        print("Current Balance: ",self.balance)
Owner = input("Enter Owner: ")
Balance = float(input("Enter Balance: "))
Account = BankAccount(Owner,Balance)
choice = "0"
while(choice!= "4"):
    print(f"(What do you want to do:),(1.Deposite),(2.Withdraw),(3.Check Balance),(4.exit)")
    choice = (input("Choose(1,2,3):"))
    if choice == "1":
        Account.deposite()
    elif choice == "2":
        Account.withdraw()
    elif choice == "3":
        Account.check_balance()
    elif choice == "4":
        exit()
    else:
        print("Wrong Option")