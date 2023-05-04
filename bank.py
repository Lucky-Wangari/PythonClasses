class Account:
    type = "Savings"
    def __init__(self, balance, number, password):
        self.balance = balance
        self.number = number
        self.password = password
    def money_remaining(self):
        return f"An account {self.balance} worth a fortune."
    def retain_your(self):
        return f"Do not forget or share your account {self.number}."
    def type_of(self):
        return f"Use strong {self.password} to avoid being hacked."        