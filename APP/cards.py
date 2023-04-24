class card:
    def __init__(self, value, suit):
        self.amount = value
        self.suit = 'DSCH'[suit]
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] [value -1]
    
    def total(self):
        if self.amount >= 10:
            return 10
        if self.amount == 1:
            return 11
        return self.amount
    
    def show(self):
        print(f'{self.value}, {self.suit}')