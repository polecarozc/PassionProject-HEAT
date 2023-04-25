import logic
from players import player
from decks import deck

class game:
    def __init__(self):
        self.decks = deck()
        self.decks.create_deck()
        self.player = player(False, self.decks)
        self.dealer = player(True, self.decks)

    def play(self):
        player_state = self.player.deal_cards()
        dealer_state = self.dealer.deal_cards()

        self.dealer.dealers_cards()
        self.player.show_cards()

        if player_state == 1:
            print('BLACKJACK')
            if dealer_state == 1:
                print('DEALER GOT BLACKJACK... ITS A PUSH!')

        choice = ''
        while choice != 'stand':
            bust = 0
            choice = input('hit or stand?: ')

            if choice == 'hit':
                bust = self.player.hit()
                self.player.show_cards()
            if bust == 1:
                return 'player busted, gg'
        self.dealer.show_cards()
        if dealer_state == 1:
            print('dealer got blackjack, gg')
            return 1

        while self.dealer.score_count() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show_cards()
                print('dealer busted, gg')
                return 1
            self.dealer.show_cards()
        if self.dealer.score_count() == self.player.score_count():
            print('push!!!!!')
        elif self.dealer.score_count() > self.player.score_count():
            print('dealer wins, gg')
        elif self.dealer.score_count() < self.player.score_count():
            print('u win, gg')

blackjack = game()
blackjack.play()