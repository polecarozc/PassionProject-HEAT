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
        setbet = int(input(f'SET A BET BETWEEN ${self.minbet}----${self.maxbet}: '))
        insurancebet = 0

        dealer_state = self.dealer.deal_cards()
        player_state = self.player.deal_cards()

        if self.dealer.check_ace()==1:
            if input('DEALER HAS AN ACE, DO YOU WANT INSURANCE?: ') == 'yes':
                print(f'INSURANCE PURCHASED FOR {setbet/2}')
                self.bankroll -= setbet/2
                insurancebet = setbet/2

        self.dealer.dealers_cards()
        self.player.show_cards()

        if self.player.check_split()==1:
            if input(f'YOU HAVE 2 {self.player.cards[0].amount}s, DO YOU WANT TO SPLIT: ') == 'yes':
                'TEST PASSED, GAME ACKKNOLEDGED SPLIT'



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
            return self.bankroll + insurancebet * 2
        else:
            choice = ''
            while choice != 'stand' and player_state != 1:
                is_bust = 0
                if choice == 'double' or is_bust == 2 or choice == 'stand':
                    break

                if len(self.player.cards) >= 3:
                    choice = input('hit or stand?: ')
                elif len(self.player.cards) <= 2 and choice != 'double' or choice != 'stand':
                    choice = input('hit,stand, or double?: ')

                if choice == 'hit':
                    is_bust = self.player.hit()
                    self.player.show_cards()
                if choice == 'double':
                    self.bankroll -= setbet
                    setbet *= 2
                    print(f'YOUR BET HAS NOW BEEN DOUBLED TO ${setbet}')
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
                    break
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
                self.bankroll += setbet * 2
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
                    self.bankroll += setbet * 2
                    return self.bankroll
                self.dealer.show_cards()
            if self.dealer.score_count() == self.player.score_count() and self.dealer.score_count() >= 17:
                print('push!!!!!\n--------')
            elif self.dealer.score_count() > self.player.score_count() and self.dealer.score_count() >= 17:
                print('dealer wins, gg\n--------')
                self.bankroll -= setbet
            elif self.dealer.score_count() < self.player.score_count() and self.dealer.score_count() >= 17:
                print('u win, gg\n--------')
                self.bankroll += setbet * 2
            self.player.cards.clear()
            self.dealer.cards.clear()
            return self.bankroll




