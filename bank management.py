class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.minimum_withdraw = 1000
        self.maximum_withdraw = 50000

    def get_balance(self):
        return self.balance
    def withdraw (self,amount):
        if amount < self.minimum_withdraw:
            return f"You cannot withdraw less than {self.minimum_withdraw} Taka"
        elif amount > self.maximum_withdraw:
            return f"You cannot withdraw more than {self.maximum_withdraw} Taka"
        elif amount > self.balance:
            return "Sorry! You do not have enough money"
        else:
            self.balance = self.balance-amount
            return f"Here is your money :{self.balance}"
    def deposit(self, amount):
        self.balance = self.balance + amount


def menu():
        print("[<<< Menu >>>]")
        print("1-> How much money do you want to add")
        print("2-> Current balance")
        print("3-> Withdraw")
        print("4-> Deposite")
        print("5-> EXIT")

while 1:
    menu()
    option=int(input("Enter your option: "))

    if option==1:
        print("Enter amount: ")
        my_bank = Bank(int(input()))

    elif option==2:
        print("Your current balance: ")
        print(my_bank.get_balance())
       
    
    elif option==3:
        print("How much money do you want to withdraw?:")
        reply = my_bank.withdraw(int(input()))
        print(reply)
        

    elif option==4:
        print("How much money do you want to deposite?: ")
        my_bank.deposit(int(input()))
        print(my_bank.get_balance())
        
    elif option==5:
        break

    else:
        print("Invalid")