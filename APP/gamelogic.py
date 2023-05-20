from players import player
from decks import deck
class game_logic:
    def __init__(self,bankroll, shoe_size, minbet, maxbet, shuffler):
        self.decks = deck()
        self.decks.create_deck()
        self.player = player(False, self.decks)
        self.dealer = player(True, self.decks)
        self.bankroll = bankroll
        self.shoe_size = shoe_size
        self.minbet = minbet
        self.maxbet = maxbet
        self.shuffler = shuffler
        self.bet = 0

    def check_split(self):
        if self.player.cards[0].amount == self.player.cards[1].amount:
            return 1
    def check_ace(self):
        if self.dealer.cards[0].amount in [1,11,'A']:
            self.insurance_purchase()
        else:
            return 2

    def insurance_purchase(self):
        if self.decks.count/self.shoe_size >=3:
            print(f'INSURANCE PURCHASED FOR {self.bet / 2}')
            self.bankroll -= self.bet / 2
            self.bet = self.bet/2
            return 1
        else:
            return 2

    def check_blackjack(self, p_state, d_state):
        if p_state == 1:
            print('YOU GOT BLACKJACK')
            self.player.show_cards()
            self.player.cards.clear()
            self.dealer.cards.clear()
            if d_state == 1:
                print('DEALER GOT BLACKJACK TOO... ITS A PUSH!\n--------')
                self.dealer.dealers_cards()
                self.player.cards.clear()
                self.dealer.cards.clear()
                return 1
            return 2
        elif d_state == 1:
            print('dealer got blackjack\n--------')
            self.dealer.show_cards()
            self.player.cards.clear()
            self.dealer.cards.clear()
            return 3
        else:
            return 4
    def next_move(self):
        choice = ''
        while choice != 'stand' and self.player_state != 1:
            is_bust = 0
            choice = input('hit or stand?: ')

            if choice == 'hit':
                is_bust = self.player.hit()
                self.player.show_cards()
            if is_bust == 1:
                print('player busted, gg\n--------')
                self.player.cards.clear()
                return 1
            if is_bust == 2:
                print('you have 21!\n--------')
                self.player.cards.clear()
                return 2
        self.dealer.show_cards()

    def dealers_move(self):
        while self.dealer.score_count() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show_cards()
                print('dealer busted, gg\n--------')
                self.player.cards.clear()
                return 1
            self.dealer.show_cards()
            if self.dealer.score_count() == self.player.score_count():
                print('push!!!!!\n--------')
            elif self.dealer.score_count() > self.player.score_count():
                print('dealer wins, gg\n--------')
            elif self.dealer.score_count() < self.player.score_count():
                print('u win, gg\n--------')
        self.player.cards.clear()