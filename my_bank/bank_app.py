from my_bank import account
from my_bank.Account_not_found import AccountNotFoundError
from my_bank.bank_class import Bank
from my_bank.invalid_amount_error import InvalidAmountError, InsufficientFundsError, InvalidPinError


class BankApp:
    def __init__(self):
        self.bank = Bank("union bank")

    def go_to_main(self):
        choices = f"""
        Welcome to union bank
        what can we do for you?
        1-> Create Account
        2-> Deposit
        3-> Withdraw
        4-> Transfer
        5-> Check Balance
        6-> Delete Account 
        7-> Exit
        """
        user_input = int(input(choices))
        match user_input:
            case 1:
                self.create_account()
            case 2:
                self.deposit()
            case 3:
                self.withdraw()
            case 4:
                self.transfer()
            case 5:
                self.check_balance()
            case 6:
                self.delete_account()
            case 7:
                exit(0)

    def create_account(self):
        first_name = input("enter your first name")
        last_name = input("enter your last name")
        pin = input("enter your pin")
        try:
            self.bank.register_customer(first_name, last_name, pin)

        finally:
            self.go_to_main()

    def deposit(self):
        account_number = int(input("enter your account number:"))
        amount = int(input("enter your amount:"))
        try:
            self.bank.deposit(account_number, amount)
            found_account = self.bank.find_account()
            print(f"account_number: {found_account.get_balance()}")
        except InvalidAmountError:
            print("Amount should be greater zero:")
        finally:
            self.go_to_main()

    def withdraw(self):
        account_number = int(input("enter your account number:"))
        amount = int(input("enter your amount:"))
        pin = (input("enter your pin:"))
        try:
            self.bank.withdraw(account_number, amount, pin)
            found_account = self.bank.find_account()
            print(f"account_number:{found_account.withdraw()}")
        except InsufficientFundsError:
            print("InsufficientFundsError:")

        except InvalidAmountError:
            print("InvalidAmountError:")

        except InvalidPinError:
            print("InvalidPinError")

        finally:
            self.go_to_main()

    def transfer(self):
        sender_account_number = int(input("enter sender account number:"))
        receiver_account_number = int(input("enter receiver account number:"))
        amount = int(input("enter your amount:"))
        pin = input("enter your pin:")
        try:
            self.bank.transfer(sender_account_number, receiver_account_number, amount, pin)
        except AccountNotFoundError:
            print("account not found")

        except InsufficientFundsError:
            print("Insufficient funds error")

        except InvalidPinError:
            print("Invalid pin found error")
        finally:
            self.go_to_main()

    def check_balance(self):
        account_number = int(input("enter your account number"))
        pin = input("enter your pin")
        try:
            print(self.bank.check_balance(account_number, pin))
        except AccountNotFoundError:
            print("account not found")

        except InvalidPinError:
            print("Invalid pin error")

    def remove_account(self):
        account_number = int(input("enter your account number"))
        pin = input("enter your pin")
        try:
            self.bank.remove_account(account_number, pin)

        except AccountNotFoundError:
            print("account not found")

        except InvalidPinError:
            print("Invalid pin error")
        finally:
            self.go_to_main()


app = BankApp()
app.go_to_main()
