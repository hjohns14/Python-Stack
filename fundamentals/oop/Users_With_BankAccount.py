
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
            self.balance = (self.interest*self.balance) + self.balance
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

class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.accounts = {
            "primary": BankAccount(2, 0)
        }

    def make_deposit(self, account_name: str, amount: int):
        self.accounts[account_name.lower()].deposit(amount)
    
    def make_withdrawal(self, account_name: str, amount: int):
        self.accounts[account_name.lower()].withdraw(amount)
    
    def display_balances(self):
        print(f"Accounts for {self.name}")
        for key, val in self.accounts.items():
            print(key.capitalize(), val.balance, sep=": $")
    
    def create_account(self, name: str, initial_deposit=0):
        if type(name) == str:
            self.accounts[name.lower()] = BankAccount(2, initial_deposit)
        else:
            print("Invalid Input in account creation!")

    #obviously i didnt finish reading the Bonus challenge instructions.....
    def transfer(self, trans_from: str, trans_to: str, amount: int):
        self.accounts[trans_from.lower()].withdraw(amount)
        self.accounts[trans_to.lower()].deposit(amount)
    
    #Bonus Challenge!
    def transfer_money(self, account_name, amount, other_user):
        self.accounts[account_name.lower()].withdraw(amount)

        other_user.make_deposit("Primary", amount)


user1 = User("Steve", "rogers@mail.com")
user2 = User("Jim", "email@email.com")
user1.make_deposit("Primary",500)
user1.create_account("Checking", 200)
user1.create_account("Savings", 500000000)
user1.display_balances()
user1.make_deposit("Checking", 1000)
user1.display_balances()
user1.make_withdrawal("Savings", 305670830)
user1.display_balances()
user1.transfer("Checking", "Primary", 300)
user1.display_balances()

user1.transfer_money("Savings", 300000, user2)
user2.display_balances()

