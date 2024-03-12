from my_bank.Account_not_found import AccountNotFoundError
from my_bank.account import Account
from my_bank.invalid_amount_error import InvalidPinError


class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
        self.number_of_account = 0

    def register_customer(self, first_name, last_name, pin):
        account_number = self.generate()
        account = Account(first_name + " " + last_name, pin, account_number)

        self.accounts.append(account)
        return account

    def find_account(self, number) -> Account:
        for account in self.accounts:
            if account.get_account_number() == number:
                return account
        raise AccountNotFoundError("Account not found error")

    def check_account_list(self):
        return len(self.accounts)

    def deposit(self, account_number: int, amount: int):
        found_account = self.find_account(account_number)
        found_account.deposit(amount)

    def check_balance(self, account_number: int, pin: str) -> int:
        found_account = self.find_account(account_number)
        return found_account.get_balance(pin)

    def withdraw(self, account_number, amount, pin):
        found_account = self.find_account(account_number)
        found_account.withdraw(amount, pin)

    def transfer(self, sender_account_number: int, receiver_account_number: int, amount: int, pin: str):
        found_account = self.find_account(sender_account_number)
        found_account1 = self.find_account(receiver_account_number)
        found_account.withdraw(amount, pin)
        found_account1.deposit(amount)

    def remove_account(self, number, pin):
        found_account = self.find_account(number)
        if found_account.get_pin() != pin:
            raise InvalidPinError("InvalidPin")
        self.accounts.remove(found_account)

    def generate(self):
        self.number_of_account += 1
        return self.number_of_account

