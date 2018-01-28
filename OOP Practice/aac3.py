#OOP hands on 


class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
        """This class generates checking account objects"""

        type = "checking"

        def __init__(self, filepath, fee):
            Account.__init__(self, filepath)
            self.fee = fee

        def transfer(self, amount):
            self.balance = self.balance - amount - self.fee


jacks_checking = Checking("jack.txt", 1)
jacks_checking.transfer(10)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

john_checking = Checking("john.txt", 1)
john_checking.transfer(10)
print(john_checking.balance)
john_checking.commit()
print(john_checking.type)

print(john_checking.__doc__)






