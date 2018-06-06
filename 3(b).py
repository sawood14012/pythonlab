class Account:

    def __init__(self, curbalance, a, r=0.5):
        self.bal = curbalance
        self.rate = r
        self.accno = a
        self.fee = 0

    def deposit(self, amt):
        self.bal = self.bal + amt
        print("After depositing you have:", self.bal)

    def add_interest(self):
        self.bal += (self.rate * self.bal)
        return self.bal

    def withdraw(self, amt):
        if amt > self.bal:
            self.fee += 100
            self.bal -= amt
            self.bal -= self.fee
            print("Amount overdrawn ,Fee charged is:", self.fee)
            print("The money remaining in ur account after fee deduction is: ", self.bal)
        else:
            self.bal -= amt
            print("Amount left in ur account is:", self.bal)


user = Account(1000, 'AC123')
ch = 1
while ch == 1:
    op = int(input("\n 1. To deposit \n 2. To withdraw\n 3.exit"))
    if op == 1:
        amt = int(input("Enter amount to be deposited"))
        user.deposit(amt)

    elif op == 2:
        amt = int(input("Enter amount to be withdrawn"))
        user.withdraw(amt)
    elif op == 3:
        break


print("\n Adding interest to your account after all the transactions now you have: ", user.add_interest())