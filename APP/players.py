from decks import deck
class player:
    def __init__(self,dealer,decks):
        self.cards = []
        self.dealer = dealer
        self.decks = decks
        self.score = 0

    def hit(self):
        self.cards.extend(self.decks.draw_card(1))
        self.score_count()
        if self.score > 21:
            return 1
        elif self.score ==21:
            return 2
        return 0

    def score_count(self):
        aces = 0
        self.score = 0
        for card in self.cards:
            if card.total() == 11:
                aces += 1
            self.score += card.total()

        while aces > 0 and self.score > 21:
            aces -= 1
            self.score -= 10
        return self.score
    
    def deal_cards(self):
        self.cards.extend(self.decks.draw_card(2))
        self.score_count()
        if self.score == 21:
            return 1
        return 0

    def dealer_gate(self):
        return 1

    def clear_deck(self):
        self.cards.clear()

    def show_cards(self):
        if self.dealer:
            print('Dealers cards')
        else:
            print('Players cards')
        for i in self.cards:
            i.show()
        print('score: ' + str(self.score))

    def dealers_cards(self):
        print('Dealers cards')
        if self.dealer_gate():
            for i in self.cards:
                i.show()
                if len(self.cards)>1:
                    break


