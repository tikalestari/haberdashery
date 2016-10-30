class BankAccount():
    def __init__(self, balance=0):
        pass

    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        pass

    def balance(self):
        pass

    def __add__(self, other):
        pass


example = BankAccount() # balance = 0
example_2 = BankAccount(3) # balance = 3
example.deposit(3) # add 3 dollars to bank account
example.withdraw(2) # remove 2 dollars from bank account
example.balance() # returns 1 (the bank account balance)
example + example_2 # returns new bank account with balance 4
