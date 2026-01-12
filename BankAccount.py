class BankAccount:
    def __init__(self,accountNumber,accountHolder,balance): #------------Done
        self.accountNumber=accountNumber
        self.accountHolder=accountHolder
        self.balance=balance

    def deposit(self, balance):
        self.balance=self.balance+balance

    
    def withdraw(self, balance):
        self.balance=self.balance-balance
    
    
    def SetBalance(self, blalance):
        self.balance=blalance
    def GetBalance(self):
        return self.balance
    
    def SetAccountNumber(self,accountNumber):
        self.accountNumber=accountNumber

    def GetAccountNumber(self):
        return self.accountNumber
    
    def SetAccountHolder(self,accountHolder):
        self.accountHolder=accountHolder

    def GetAccountHolder(self):
        return self.accountHolder 
    
    def GetDetail(self):
        print(f"Account Holder is {self.accountHolder} and account Number is {self.accountNumber} and Balance {self.balance}")