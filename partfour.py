# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name.
#  Show that it affects all instances.

# solution

class Bank:
    bank_name = "UBL"
    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

account1 =Bank("Ali") 
account2 =Bank("Bilal")

account1.display()
account2.display()

Bank.change_bank_name("Default Bank")

account1.display()
account2.display()

         