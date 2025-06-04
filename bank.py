class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited R{amount:.2f}. New balance: R{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew R{amount:.2f}. Remaining balance: R{self.balance:.2f}")

    def display_balance(self):
        print(f"{self.owner}'s balance: R{self.balance:.2f}")

if __name__ == "__main__":
    account = BankAccount("Alex", 500.00)
    account.display_balance()

    account.deposit(150.00)
    account.withdraw(100.00)
    account.withdraw(600.00)
    account.display_balance()
