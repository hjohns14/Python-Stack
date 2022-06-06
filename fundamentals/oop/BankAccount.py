class BankAccount:

    accounts = []

    def __init__(self, percent_interest, amount=0) -> None:
        self.balance = amount
        self.interest = percent_interest/100
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if BankAccount.check_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient Funds. Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        percent_interest = round(self.interest*100)
        print(f"Balance: {self.balance}", f"Interest: {percent_interest}%", sep="\n", end="\n\n")
        return self

    def yeild_interest(self):
        if self.balance > 0:
            self.balance = self.interest*self.balance + self.balance
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.accounts:
            print(f"Balance {account.balance}  -- Interest: {account.interest}")
        

    @staticmethod
    def check_withdraw(balance, withdraw_ammount):
        if balance - withdraw_ammount > 0:
            return True
        else: return False

account1 = BankAccount(5, 100)
account2 = BankAccount(1, 5000)
account1.deposit(200).deposit(130).deposit(370).withdraw(500).yeild_interest().display_account_info()
account2.deposit(500).deposit(1000).withdraw(1500).withdraw(250).withdraw(250).withdraw(7500).yeild_interest().display_account_info()

BankAccount.display_all_accounts()


