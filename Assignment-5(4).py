class Account:

    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance

class SavingsAccount(Account):

    def __init__(self,title=None,Balance=0,interestrate=0):
        super().__init__(title, Balance)
        self.interestrate=interestrate

account = Account("Ashish", 5000)

print("Account Title:", account.title)
print("Account Balance:", account.Balance)

savings_account = SavingsAccount("Ashish", 5000, 5)

print("Savings Account Title:", savings_account.title)
print("Savings Account Balance:", savings_account.Balance)
print("Interest Rate:", savings_account.interestrate)
