class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi! My name is {self.name}")
me = User('Michael')
me.greet()
class BankAccount:
    def __init__(self, account_type, starting_balance):
        self.type = account_type
        self.balance = starting_balance
        self.overdraft_fees = 0
        self.default_interest = .02
    def withdraw(self, amount):
        if amount < 0:
            return False
        else:
            net_balance = self.balance - amount - self.overdraft_fees
            self.balance -= amount if net_balance >= -100 else 0
            if net_balance < -100:
                print("This is hitting the insufficient funds")
                return 'Insufficient Funds'
            if self.balance < 0:
                self.overdraft_fees += 20
            print(f"The withdrawal amount is {amount}")
            print(f"The balance is {self.balance}")
            return amount
    def deposit(self, amount):
        if amount < 0:
            return False
        else:
            self.balance += amount
            print(f"The balance is {self.balance} in your {self.type} account")
            return self.balance
    def accumulated_interest(self):
        self.balance += (self.balance * self.default_interest)
        print(f"Your new balance after accumulated interest in your {self.type} account is {self.balance}")
    def balance_total(self):
        return self.balance
    ## Add balance from the account being called to an account being added
    def __add__(self, other_account):
        return self.balance + other_account.balance_total()
    def __sub__(self, other_account):
        return self.balance - other_account.balance_total()
    def __mul__(self, other_account):
        return self.balance * other_account.balance_total()
    def __truediv__(self, other_account):
        return self.balance / other_account.balance_total()
    def __eq__(self, other_account):
        return self.balance == other_account.balance_total()
chase = BankAccount("checking", 500)
boa = BankAccount('checking2', 500)
account_add = boa.balance_total() + chase.balance_total()
balance_both = chase + boa
balance_subst = chase - boa
balance_mult = chase * boa
balance_div = chase / boa
balance_le = chase == boa

print(f"Your combined account balance is {balance_both}")
print(f"The difference between your chase account and BoA account is {balance_subst}")
print(f"Multiplying the balance between both of your accounts would give you {balance_mult}")
print(f"Divinding the balance in your Chase account and your BoA account equals {balance_div} ")
print(f"Does your balance at Chase and BoA equal to each other? {balance_le}")
chase.deposit(600)
print(f"Chase account has ${chase.balance}")
print(chase.withdraw(200))
print(f"Chase account has ${chase.balance}, after previous withdrawal")
print(chase.accumulated_interest())
print(f"Chase account has a ${chase.balance}, after receiving an accumulated interest")

class Child_Account(BankAccount):
    def __init__(self, account_type, starting_balance):
        super().__init__(account_type, starting_balance)
    def child_interest(self):
        super().accumulated_interest()
        self.balance += 10
        print(f"Your new balance after child account accumulated interest in your {self.type} account is ${self.balance}")
        return self.balance

child_chase = Child_Account("savings", 200)
print(child_chase.withdraw(100))
print(child_chase.child_interest())
class OverdraftAccount(BankAccount):
    def __init__(self, account_type, starting_balance):
        super().__init__(account_type, starting_balance)
    def overdraft_penalty(self, amount):
        super().withdraw(amount)
        if self.balance < 0:
            self.balance -= 40
            print(f'Your new balance in your {self.type} account after withdrawal and overdraft penalty (-$40) is ${self.balance}')
        return False
    
over_chase = OverdraftAccount('bad_credit', 400)
print(over_chase)
print(over_chase.overdraft_penalty(450))


