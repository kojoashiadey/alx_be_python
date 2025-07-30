# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize a new bank account with an optional initial balance."""
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw an amount if sufficient balance is available.
        Returns True if successful, otherwise False.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
