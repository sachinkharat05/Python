from.BankAccount import BankAccount

class FixedDeposit(BankAccount):
    def __init__(self, accountNumber, accountHolder, balance, tenureYears, interestRate=6):
        super().__init__(accountNumber, accountHolder, balance)
        self.tenureYears = tenureYears
        self.interestRate = interestRate

    def CalculateMaturityAmount(self):
        amount = self.balance * (1 + self.interestRate / 100) ** self.tenureYears
        return round(amount, 2)