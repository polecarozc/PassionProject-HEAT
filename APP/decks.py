from cards import card; import random

class deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        for i in range(1,14):
            for j in range(4):
                self.cards.append(card(i,j))


    def draw_card(self, rep):
        hand = []
        for i in range(rep):
            card = random.choice(self.cards)
            self.cards.remove(card)
            hand.append(card)
        print('number of cards ' + str(len(self.cards)))
        return hand
    
    def deck_count(self):
        return len(self.cards)