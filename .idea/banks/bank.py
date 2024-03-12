from account import Account
class Bank:
    def __init__(self, name):
        self.name = self.name
        self.accounts = []
        self.number = 0


    def register_customer(self, firstname: str, lastname: str, pin: str) -> None:
        generated = self.generate()
        account = Account(firstname + " " + lastname, pin,generated )
        self.account += account


    def find_account(self,number):
        for account in self.accounts:
            if account.getnumber()  ==  number:
                return account

    def generate(self):
        self.number += 1
        return number

    def deposit(self,number,amount):
        found_account = self.find_account(number)
        found_account.deposit(amount)


    def withdraw(self,number,pin,amount):
        found_amount = self.find_account(number)
        found_acount.withraw(amount)

    def transfer(self,senders_number,receivers_number,amount,pin,):
        found_acount = self.find_account(senders_number)
        found_acount2 = self.find_account(receivers_number)
        found_acount.withraw(amount,pin)
        found_acount2.deposit(amount,pin)


    def check_balance(self,number,pin):
        if(slf_pin == 0):
            return self.balance


    def remove_account(self,number,pin):
        found_account = self.find_account(number)
        if found_account.pin ==pin:
            self.accounts.remove(found_account)










