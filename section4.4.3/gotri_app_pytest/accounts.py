class CommuterAccount:

    def __init__(self, id):
        self.id = id
        self.balance = 0

    def add(self, amount):
        self.balance += amount

    def pay(self, amount):
        if (amount > self.balance):
            raise ValueError('The payment amount is greater than the balance')
        self.balance -= amount
