import cards; import random

class deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        self.cards.append(cards([(i,j) for i in range(1,14) for j in range(4)]))

    def draw_card(self, rep):
        cards = [self.cards.pop(random.choice(self.cards)) for _ in range(rep)]
        return cards
    
    def deck_count(self):
        return len(self.cards)