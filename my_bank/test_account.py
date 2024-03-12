import unittest

from my_bank.account import Account
from my_bank.invalid_amount_error import InvalidAmountError, InsufficientFundsError, InvalidPinError


class MyTestCase(unittest.TestCase):
    def test_deposit(self):
        account = Account("marvellous", "1234", 1)
        account.deposit(500)
        self.assertEqual(500, account.get_balance("1234"))

    def testNegativeDeposit(self):
        account = Account("marvellous", "1234", 1)
        with self.assertRaises(InvalidAmountError):
            account.deposit(-500)

    def test_withdrawal_decreases_balance(self):
        account = Account("marvellous", "1234", 1)
        account.deposit(500)
        self.assertEqual(500, account.get_balance("1234"))
        account.withdraw(300, "1234")
        self.assertEqual(200, account.get_balance("1234"))

    def test_for_negative_amount_withdraw(self):
        account = Account("marvellous", "1234", 1)
        account.deposit(500)
        self.assertEqual(500, account.get_balance("1234"))
        with self.assertRaises(InvalidAmountError):
            account.withdraw(-200, "1234")
        self.assertEqual(500, account.get_balance("1234"))

    def test_for_withdrawing_amount_greater_than_balance(self):
        account = Account("marvellous", "1234", 1)
        account.deposit(100)
        with self.assertRaises(InsufficientFundsError):
            account.withdraw(1000, "1234")

    def test_for_withdrawal_with_invalid_pin(self):
        account = Account("marvellous", "1234", 1)
        account.deposit(500)
        with self.assertRaises(InvalidPinError):
            account.withdraw(200, "555")

    def test_for_checking_balance_with_invalid_pin(self):
        account = Account("marvellous", "1234", 1)
        account.deposit(200)
        with self.assertRaises(InvalidPinError):
            account.get_balance("555")
