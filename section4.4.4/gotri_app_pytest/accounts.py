class CommuterAccount:

    def __init__(self, id):
        self.id = id
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def add(self, amount):
        self._balance += amount

    def pay(self, amount):
        if (amount > self._balance):
            raise ValueError('The payment amount is greater than the balance')
        self._balance -= amount
