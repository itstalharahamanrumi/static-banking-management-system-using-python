class Banking:
    def __init__(self, username, initial_balance):
        self.name = username
        self.balance = initial_balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            return amount

    def get_balance(self):
        return self.balance


    def widthraw (self, amount):
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return f"Insufficient Balance. "






My_Account = Banking ("My_Account", 76000)
print(f"Account Name: {My_Account.name}")
print(f"Initial Balance is:  {My_Account.balance}")
print(f"Deposti Balance :  {My_Account.deposit(amount=2000)}")
print(f"After Deposti, The Balance ia :  {My_Account.get_balance()}")
print(f"Withdraw Balance :  {My_Account.widthraw(amount=3000)}")
print(f"After Withdraw, The Balance is :  {My_Account.get_balance()}")
