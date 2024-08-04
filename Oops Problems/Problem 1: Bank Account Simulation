class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        # Initialize the bank account with account number, owner, and balance
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Add the deposit amount to the balance
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        # Check if there are sufficient funds for withdrawal
        if amount > self.balance:
            print("Insufficient funds")
        else:
            # Deduct the withdrawal amount from the balance
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        # Return the current balance of the account
        return self.balance

if __name__ == "__main__":
    # Create a BankAccount instance with initial balance
    account = BankAccount("123456789", "Alice", 1000)
    
    # Perform deposit and withdrawal operations
    account.deposit(500)
    account.withdraw(200)
    
    # Print the final balance
    print(f"Final balance: {account.get_balance()}")
