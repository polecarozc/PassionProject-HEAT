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
        if self.bankroll < self.minbet:
            return 10
        print(f'YOUR BANKROLL IS : ${self.bankroll}')
        setbet = int(input(f'SET A BET BETWEEN {self.minbet}----{self.maxbet}: '))

        dealer_state = self.dealer.deal_cards()
        player_state = self.player.deal_cards()

        self.dealer.dealers_cards()
        self.player.show_cards()

        if player_state == 1:
            print('YOU GOT BLACKJACK')
            self.player.cards.clear()
            self.dealer.cards.clear()
            if dealer_state == 1:
                self.dealer.show_cards()
                print('DEALER GOT BLACKJACK... ITS A PUSH!\n--------')
                self.player.cards.clear()
                self.dealer.cards.clear()
                return self.bankroll
            self.bankroll += (setbet * 3/2)
            return self.bankroll
        elif dealer_state == 1:
            self.dealer.show_cards()
            print('dealer got blackjack\n--------')
            self.player.cards.clear()
            self.dealer.cards.clear()
            self.bankroll -= setbet
            return self.bankroll
        else:
            choice = ''
            while choice != 'stand' and player_state != 1:
                is_bust = 0
                choice = input('hit or stand?: ')

                if choice == 'hit':
                    is_bust = self.player.hit()
                    self.player.show_cards()
                if is_bust == 1:
                    print('player busted, gg\n--------')
                    self.player.cards.clear()
                    self.dealer.cards.clear()
                    self.bankroll -= setbet
                    return self.bankroll
                if is_bust == 2:
                    print('you have 21!,\n--------')
            self.dealer.show_cards()
            if dealer_state == 1:
                print('dealer got blackjack, gg\n--------')
                self.player.cards.clear()
                self.dealer.cards.clear()
                self.bankroll -= setbet
                return self.bankroll

            if self.player.score_count() > self.dealer.score_count() and self.dealer.score_count() >= 17:
                print('player wins, gg\n--------')
                self.player.cards.clear()
                self.dealer.cards.clear()
                self.bankroll += setbet
                return self.bankroll
            elif self.player.score_count() < self.dealer.score_count() and self.dealer.score_count() >= 17:
                print('dealer wins, gg\n--------')
                self.player.cards.clear()
                self.dealer.cards.clear()
                self.bankroll -= setbet
                return self.bankroll
            while self.dealer.score_count() < 17:
                if self.dealer.hit() == 1:
                    self.dealer.show_cards()
                    print('dealer busted, gg\n--------')
                    self.player.cards.clear()
                    self.dealer.cards.clear()
                    self.bankroll += setbet
                    return self.bankroll
                self.dealer.show_cards()
            if self.dealer.score_count() == self.player.score_count() and self.dealer.score_count() >= 17:
                print('push!!!!!\n--------')
            elif self.dealer.score_count() > self.player.score_count() and self.dealer.score_count() >= 17:
                print('dealer wins, gg\n--------')
                self.bankroll -= setbet
            elif self.dealer.score_count() < self.player.score_count() and self.dealer.score_count() >= 17:
                print('u win, gg\n--------')
                self.bankroll += setbet
            self.player.cards.clear()
            self.dealer.cards.clear()
            return self.bankroll




