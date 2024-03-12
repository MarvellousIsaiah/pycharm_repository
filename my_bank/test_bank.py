import unittest

from my_bank.bank_class import Bank
from my_bank.invalid_amount_error import InvalidPinError, InsufficientFundsError, InvalidAmountError


class MyTestCase(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.account = None

    def test_registerCustomer_listOfAccountIncreases(self):
        bank = Bank("union bank")
        self.assertEqual(0, bank.check_account_list())
        bank.register_customer("marvy", "isaiah", "1234")
        self.assertEqual(1, bank.check_account_list())

    def test_deposit(self):
        bank = Bank("union bank")
        bank.register_customer("marvy", "isaiah", "1234")
        bank.deposit(1, 1000)
        print(bank.accounts)
        self.assertEqual(1000, bank.check_balance(1, "1234"))

    def test_withdraw(self):
        bank = Bank("union bank")
        bank.register_customer("marvy", "isaiah", "1234")
        bank.deposit(1, 1000)
        bank.withdraw(1, 500, "1234")
        self.assertEqual(500, bank.check_balance(1, "1234"))

    def test_transfer(self):
        bank = Bank("union bank")
        bank.register_customer("marvy", "isaiah", "1234")
        bank.register_customer("marvy", "marv", "1235")
        bank.deposit(1, 1000)
        bank.transfer(1, 2, 100, "1234")
        self.assertEqual(bank.check_balance(2, "1235"), 100)

    def test_check_balance(self):
        bank = Bank("union")
        bank.register_customer("marvy", "isaiah", "1234")
        bank.deposit(1, 200)
        self.assertEqual(bank.check_balance(1, "1234"), 200)

    def test_remove_account(self):
        bank = Bank("union bank")
        bank.register_customer("marvy", "isaiah", "1234")
        bank.register_customer("marvy", "marv", "1235")
        bank.remove_account(2, "1235")
        self.assertEqual(bank.check_balance(1, "1234"), 0)

    def test_invalid_withdraw_with_invalid_pin(self):
        bank = Bank("union bank")
        bank.register_customer("marvy", "isaiah", "1234")
        bank.deposit(1, 500)
        self.assertRaises(InvalidPinError, lambda: bank.check_balance(1, "1235"))

    def test_for_withdrawing_amount_greater_than_balance(self):
        bank = Bank("union bank")
        bank.register_customer("marvy", "isaiah", "1234")
        bank.deposit(1, 500)
        self.assertRaises(InsufficientFundsError), lambda: bank.withdraw(1, 1000, "1234")

    def test_for_negative_amount_withdraw(self):
        bank = Bank("uba")
        bank.register_customer("marvy", "isaiah", "1234")
        bank.deposit(1, 1000)
        self.assertRaises(InvalidAmountError), lambda: bank.withdraw(-2000)

    def test_removeAccountWithIncorrectPin(self):
        bank = Bank("gtb")
        bank.register_customer("marvy", "isaiah", "1234")
        self.assertRaises(InvalidPinError),lambda:bank.remove_account(1,"1255")



if __name__ == '__main__':
    unittest.main()
