from.BankAccount import BankAccount
class CurrentAccount(BankAccount):
        def __init__(self,accountNumber,accountHolder,balance,limit=1000):
         super().__init__(accountNumber,accountHolder,balance)
         self.limit=limit

        9
         
         pass