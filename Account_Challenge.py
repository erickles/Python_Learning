class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f"Added {deposit_amount} to the balance")

    def withdrawal(self,withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance = self.balance -= withdrawal_amount
            print("Withdrawal accepted")
        else:
            print("Sorry non enough funds!")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

a = Account('Erick Souza',100000)

print(a)

a.deposit(100)

print(a)

a.withdrawal(800)

print(a)

a.withdrawal(80000000)