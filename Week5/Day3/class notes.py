class BankAccount():
    bank_name = 'leumi-achim'
    withdrawl_fee_percent = 5/100
    minus_fee_percent = 2/100
    def __init__(self, balance):
        self.__balance = balance
    @staticmethod
    def verify_input(text):
        valid_flag = False
        while not valid_flag:
            try:
                num = int(text)
                if num < 0:
                    raise ValueError('number cannot be negative')
                else:
                    valid_flag = True
            except ValueError:
                text = input('input a number, positive only')
        return num

    def show_balance(self):
        print(f'Current balance:{self.__balance}')

    def check_and_charge_minus(self):
        if self.__balance < 0:
            self.__balance += self.__balance * self.minus_fee_percent
            print('you were charged for being in minus, good luck')

        def deposit(self, amount):
            amount = self.verify_input(amount)
            self.__balance += amount
            self.check_and_charge_minus()

    def withdraw(self, amount):
        amount = self.verify_input(amount)
        if self.__balance < amount:
            print(f'you\'re too poor, your current max withdrawl is {self.__balance}')
        else:
            self.__balance -= amount
            fee_sum = amount * self.withdrawl_fee_percent
            self.__balance -= fee_sum
            print(f'enjoy your {amount}, we\'ve taken {fee_sum} in fees for this transaction')
            self.show_balance()
        self.check_and_charge_minus()
    def __repr__(self):
        return f'bank account, balance:{self.__balance}'
account = BankAccount(0)
account
BankAccount.deposit(account,400)
account.deposit(400)

# same but more complex which includes: property, staticmethod, classmethod
# class BankAccount():
#     bank_name = 'leumi-achim'
#     withdrawl_fee_percent = 5/100
#     minus_fee_percent = 2/100
#     taken_names = []
#     @property
#     def email(self):
#         return f'{self.owner_name}@{self.bank_name}.com'
#     def __init__(self, name, balance=0):
#         self.__balance = balance
#         self.transactions = []
#         self.owner_name = name
#         self.is_admin = False
#         self.taken_names.append(name)
#         print(f'account created for {self.owner_name}')
#     @classmethod
#     def create_account(cls, name):
#         if name in cls.taken_names:
#             print('that name is taken, try again')
#             return 
#         account = cls(name)
#         return account
#     @staticmethod
#     def verify_input(text):
#         valid_flag = False
#         while not valid_flag:
#             try:
#                 num = int(text)
#                 if num < 0:
#                     raise ValueError('number cannot be negative')
#                 else:
#                     valid_flag = True
#             except ValueError:
#                 text = input('input a number, positive only')
#         return num
#     def show_balance(self):
#         print(f'Current balance:{self.__balance}')
#     def check_and_charge_minus(self):
#         if self.__balance < 0:
#             self.__balance += self.__balance * self.minus_fee_percent
#             print('you were charged for being in minus, good luck')
#     def collect_fees_from_amount(self, amount):
#         fee_sum = amount * self.withdrawl_fee_percent
#         self.__balance -= fee_sum
#         return fee_sum
#     def create_transaction(self,a, b, c):
#         transaction = {
#             'transaction_type': c,
#             'amount': a,
#             'fees': b
#         }
#         self.transactions.append(transaction)
#     def deposit(self, amount):
#         amount = self.verify_input(amount)
#         self.__balance += amount
#         fees = self.collect_fees_from_amount(amount)
#         self.check_and_charge_minus()
#         self.create_transaction(amount, fees, 'deposit')
#     def withdraw(self, amount):
#         amount = self.verify_input(amount)
#         if self.__balance < amount:
#             print(f'you\'re too poor, your current max withdrawl is {self.__balance}')
#         else:
#             self.__balance -= amount
#             fees = self.collect_fees_from_amount(amount)
#             print(f'enjoy your {amount}, we\'ve taken {fees} in fees for this transaction')
#             self.show_balance()
#             self.create_transaction(amount, fees, 'withdraw')
#         self.check_and_charge_minus()
#     def __repr__(self):
#         return f'bank account, balance:{self.__balance}'
# account = BankAccount.create_account('Toby')
# account = BankAccount.create_account('Toby')
# account = BankAccount.create_account('Toby')
# account = BankAccount(name='Toby')
# account.deposit(400)
# account.withdraw(100)
# account.deposit(120)
# account.withdraw(150)
# account.deposit(178)