from logic import logic
from players import player
from decks import deck

class game:
    def __init__(self, bankroll, shoe_size, minbet, maxbet, shuffler):
        self.decks = deck()
        self.decks.create_deck()
        self.player = player(False, self.decks)
        self.dealer = player(True, self.decks)
        self.bankroll = bankroll
        self.shoe_size = shoe_size
        self.minbet = minbet
        self.maxbet = maxbet
        self.shuffler = shuffler


    def play(self):


        player_state = self.player.deal_cards()
        dealer_state = self.dealer.deal_cards()

        self.dealer.dealers_cards()
        self.player.show_cards()

        if player_state == 1:
            print('YOU GOT BLACKJACK')
            if dealer_state == 1:
                print('DEALER GOT BLACKJACK... ITS A PUSH!')
        elif dealer_state == 1:
            print('dealer got blackjack')
            self.dealer.show_cards()
        else:
            choice = ''
            while choice != 'stand' and player_state != 1:
                is_bust = 0
                choice = input('hit or stand?: ')

                if choice == 'hit':
                    is_bust = self.player.hit()
                    self.player.show_cards()
                if is_bust == 1:
                    print('player busted, gg')
                    return
                if is_bust == 2:
                    print('you have 21!')
                    return
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




