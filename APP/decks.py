from cards import card; import random

class deck:
    def __init__(self):
        self.cards = []
        self.count = 0

    def create_deck(self):
        for i in range(1,14):
            for j in range(4):
                self.cards.append(card(i,j))


    def draw_card(self, rep):
        hand = []
        if len(self.cards) == 0:
            print('OUT OF CARDS! Reshuffling deck\n--------')
            self.create_deck()
        for i in range(rep):
            card = random.choice(self.cards)
            self.cards.remove(card)
            hand.append(card)
            self.update_count(card)
        #print('number of cards ' + str(len(self.cards)))
        #print('the count is now ' + str(self.count))
        return hand
    def check_ace(self, card):
        if card.amount in [1,11]:
            return 1
        else:
            return 2

    def update_count(self, card):
        if card.amount in [2,3,4,5,6]:
            self.count += 1
        elif card.amount in [1, 10, 11, 12, 13]:
            self.count += -1
        print('COUNT IS ' + str(self.count))
    
    def deck_count(self):
        return len(self.cards)

