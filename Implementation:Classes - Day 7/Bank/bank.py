class BankAccount():
    def __init__(self, b):
        self.b = b

    def withdraw(self, amount):
        self.amount = amount
        self.b -= int(amount)

    def deposit(self, amount):
        self.amount = amount
        self.b += int(amount)

    def balance(self):
        return self.b

    def __add__(self, other):
        new_balance = self.balance() + other.balance()
        new_bank_acc = BankAccount(new_balance)
        return new_bank_acc

def bank():
    accounts = {}
    n,m = map(int,input().split())
    for i in range(n):
        accounts[input()] = BankAccount(0)
    for i in range(m):
        acc, func, amt = input().split()
        if func == "DEPOSIT":
            accounts[acc].deposit(amt)
        if func == "WITHDRAW":
            if accounts[acc].balance() < int(amt):
                print("NOT ENOUGH MONEY")
            else:
                accounts[acc].withdraw(amt)
        if func == "MERGE":
            accounts[acc] = accounts[acc] + accounts[amt]
            accounts[amt] = accounts[acc]
    for i, val in accounts.items():
        print(i + " balance: " + str(val.balance()))

if __name__ == "__main__":
    bank()
