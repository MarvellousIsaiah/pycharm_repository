from my_bank.invalid_amount_error import InvalidAmountError, InsufficientFundsError, InvalidPinError


class Account:

    def __init__(self, name: str, pin: str, number: int):
        self.name = name
        self.pin = pin
        self.number = number
        self.balance = 0

    def deposit(self, amount: int):
        if amount < 0:
            raise InvalidAmountError("Amount should be greater than zero")
        else:
            self.balance += amount

    def withdraw(self, amount, pin):
        if pin != self.pin:
            raise InvalidPinError("Invalid Pin")
        if amount <= 0:
            raise InvalidAmountError("Amount should be greater than zero")
        if self.balance < amount:
            raise InsufficientFundsError("InsufficientFundsError")

        self.balance -= amount

    def get_balance(self, pin):
        if self.pin != pin:
            raise InvalidPinError("Invalid Pin Error ")
        else:
            return self.balance

    def get_account_number(self):
        return self.number

    def get_pin(self):
        return self.pin



