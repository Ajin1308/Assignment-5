class Account:

    def __init__(self, title=None, Balance=0):
        self.title=title
        self.Balance=Balance

    def withdraw_amt(self, with_amt):
        self.Balance -= with_amt

    def deposite_amt(self, dep_amt):
        self.Balance += dep_amt

    def getBalance(self):
        return self.Balance
    
class SavingsAccount(Account):

    def __init__(self,title=None,Balance=0,interestrate=0):
        super().__init__(title, Balance)
        self.interestrate=interestrate

    def interestAmount(self):
        intr_amt=(self.Balance*self.interestrate)/100
        return intr_amt

savings_account = SavingsAccount("Ashish", 5000, 5)

print("Savings Account Title:", savings_account.title)
print("Savings Account Balance:", savings_account.Balance)
print("Interest Rate:", savings_account.interestrate)
#withdrawal
savings_account.withdraw_amt(500)
account_balance=savings_account.getBalance()
print("Account Balance after withdrawal: ",account_balance)
#Deposite
savings_account.deposite_amt(900)
account_balance=savings_account.getBalance()
print("Account Balance after deposite: ",account_balance)

interestAmount=savings_account.interestAmount()
print("Interest Amount: ",interestAmount)
