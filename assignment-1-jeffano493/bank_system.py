"""
This module defines a BankAccount class to represent bank accounts and provides methods for
depositing, withdrawing, displaying balances, and transferring funds between accounts.
"""
class InsufficientBalanceError(Exception):
    """Custom exception class for insufficient balance errors."""
class BankAccount:
    """Define a BankAccount class to represent bank accounts"""
    def __init__(self, name, balance=0):
        """Initialize a BankAccount object with a given name and optional initial balance of 0."""
        self.name, self.balance = name, balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print("Amount Deposited")
        else:
            raise ValueError("Amount should be greater than 0")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient balance is available."""
        if amount <= 0:
            raise ValueError("Withdrawal amount should be greater than 0")
        if amount > 0 & amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn")
        else:
            raise InsufficientBalanceError("Insufficient balance for withdrawal")

    def display_balance(self):
        """Get and return the current account balance."""
        return self.balance

    def transfer(self, amount, other_account):
        """Transfer a specified amount from this account to another account."""
        if amount < 0:
            raise ValueError("Transfer amount should be greater than or equal to 0")
        try:
            self.withdraw(amount)
            other_account.deposit(amount)
            print("Transfer Successful")
        except (ValueError, InsufficientBalanceError) as exc:
            print(f"Transfer failed: {exc}")

# Create two BankAccount instances with initial balances
n1 = BankAccount("John", 1000)
n2 = BankAccount("Doe", 500)

# Display the initial account balances
print(n1.display_balance())
print(n2.display_balance())

# Perform a transfer from account 1 to account 2
TRANSFER_AMOUNT = 200

if TRANSFER_AMOUNT < n1.display_balance():
    try:
        n1.transfer(TRANSFER_AMOUNT, n2)
    except (ValueError, InsufficientBalanceError) as exception:
        print(f"Transfer failed: {exception}")
else:
    print("Insufficient balance for transfer")

# Display updated account balances after the transfer
print(n1.display_balance())
print(n2.display_balance())
