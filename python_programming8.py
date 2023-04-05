#Que 1
#Customer Bank Acc
'''
A bank has many customers and each customer has a bank account
There are also privileged customers 
who can earn bonus points for each of their transaction. 
This scenario is depicted through the below class diagram.
30 min

Customer
- customer_id
- customer_name
- age
- account
_init_(customer_id, customer_name, age, account)
+ withdraw(amount)
+ take_card()
+ get_customer_id()
+ get_customer_name()
+ get_age()
+ get_account()
Account
- account_type
- balance
- min_balance
_init_(account_type,balance,min_balance)
+ get_account_type()
+ get_balance()
+ get_min_balance()
+ set_balance(balance)
PrivilegedCustomer
- bonus_points
_init_ (customer_id, customer_name, age, account, 
bonus_points)
+ withdraw(amount)
+ get_bonus_points()
- increase_bonus()
OverdrawException
LimitReachedException

RULES TO FOLLOW
================
Customer:
withdraw(amount): This method should reduce the account balance based on the
amount withdrawn. Raise the following exceptions based on the given conditions.
OverdrawException - If the amount to be withdrawn is greater than account balance.
LimitReach#Que 1
'''

class Customer:
    def __init__(self, customer_id, customer_name, age, account):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.age = age
        self.account = account

    def withdraw(self, amount):
        if amount > self.account.get_balance():
            raise OverDrawException("Withdraw amount is greater than account balance")
        elif self.account.get_balance() - amount < self.account.get_min_balance():
            raise LimitReachedException("Account balance is less than minimum balance")
        else:
            self.account.set_balance(self.account.get_balance() - amount)
            print("Amount withdrawn successfully")
    
    def take_card(self):
        print("Take card out from the ATM")
    def get_customer_id(self):
        return self.customer_id
    def get_customer_name(self):
        return self.customer_name
    def get_age(self):
        return self.age
    def get_account(self):
        return self.account

class Account:
    def __init__(self, account_type, balance, min_balance):
        self.account_type = account_type
        self.balance = balance
        self.min_balance = min_balance

    def get_account_type(self):
        return self.account_type
    def get_balance(self):
        return self.balance
    def get_min_balance(self):
        return self.min_balance
    def set_balance(self, balance):
        self.balance = balance

class PrivilegedCustomer(Customer):
    def __init__(self, customer_id, customer_name, age, account, bonus_points):
        super().__init__(customer_id, customer_name, age, account)
        self.bonus_points = bonus_points

    def increase_bonus(self):
        if self.account.get_balance() > 1000:
            self.bonus_points += 10
        else:
            self.bonus_points += 2

    def withdraw(self, amount):
        try:
            super().withdraw(amount)
            self.increase_bonus()
            print(f"Bonus Points: {self.bonus_points}")
        except (OverdrawException, LimitReachedException) as e:
            print(e)
        finally:
            self.take_card()

account = Account("Savings", 1000, 500)
customer = PrivilegedCustomer(100, "Gopal", 43, account, 100)
customer.withdraw(100)













































