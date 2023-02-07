class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been added to your account, new balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn, new balance: {self.balance}")


account = BankAccount("John Doe")
account.deposit(100)
account.withdraw(50)
account.withdraw(100)
