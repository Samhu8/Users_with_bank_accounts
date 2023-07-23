
class BankAccount:

    users = []

    def __init__(self, balance):
        self.int_rate = 0.02
        self.balance = balance
        BankAccount.users.append(self)

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'Your new balance is, ${self.balance}.')
        return self

    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(f'Your new balance is, ${self.balance}.')
        return self

    def display_account_info(self):
        print(f'Your interest rate is, {self.int_rate}%.')
        print(f'Your current balance is, ${self.balance}.')
        return self

    def yield_interest(self):
        rate = self.balance * self.int_rate * 12
        print(f'Your yield interest rate is ${rate}.')
        return self

    @classmethod
    def all_users(cls):
        for user in cls.users:
            user.display_account_info()

class User:
    def __init__(self,name,email,account_type):
        self.name = name
        self.email = email
        self.account_type = account_type
        self.account = BankAccount(0)

    def make_deposit(self,money,type):
        print(self.name)
        print(type)
        type = self.account.deposit(money)
        return self

    def make_withdrawal(self,money,type):
        print(self.name)
        print(type)
        type = self.account.withdraw(money)
        return self

    def display_user_balance(self,type):
        self.account.display_account_info()
        return self

    def transfer_money(self,amount,other_user):
        print(self.name)
        self.account.withdraw(amount)
        print(other_user.name)
        other_user.account.deposit(amount)
        pass


user1 = User('Hugo', 'hsam824@dojo.com',['checking','saving'])
user2 = User('Claudia','csam12@dojo.com', ['checking','saving'])
user1.make_deposit(500,user1.account_type[0]).make_withdrawal(50,user1.account_type[0]).display_user_balance(user1.account_type[0])
user1.transfer_money(100,user2)

