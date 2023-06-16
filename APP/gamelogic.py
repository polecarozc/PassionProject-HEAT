from players import player
from decks import deck
import perfect_basic_strategy as pbs
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
        self.playable_hands = []
        
    def total_split_score(self, hands):
        total = 0
        for list in self.playable_hands[hands]:
            for card in list:
                total += card.total()
        return total

    def check_split(self):
        if self.player.cards[0].amount == self.player.cards[1].amount:
            self.qualify_split()
        else:
            print('cards are not the same, player cards are {0} & {1}'.format(self.player.cards[0].value,self.player.cards[1].value))

    def qualify_split(self):
        if pbs.perfect_split(self.player.cards[0].amount, self.dealer.cards[0].amount) == 1:
            print('--------CARDS WILL BE SPLIT, players cards are {} & {}, dealers card is {}'.format(self.player.cards[0].value,self.player.cards[1].value, self.dealer.cards[0].value))
            self.playable_hands.append(self.player.cards[0])
            self.playable_hands.append(self.player.cards[1])

            print('----TEST, score for first split hand is {}'.format(self.playable_hands[0].total()))


            for i in range(2):
                total = 0
                for list in self.playable_hands[i]:
                    for card in list:
                        total += card.total()

                while pbs.hard_total(total) !=1:
                    self.player.cards.clear()
                    self.player.hit()
                    self.playable_hands.append(self.player.cards[i])





            print("players new hands are {} & {}".format(self.playable_hands[0].value, self.playable_hands[1].value))

        else:
            print('--------cards will not be split, players cards are {} & {}, dealers card is {}'.format(self.player.cards[0].value,self.player.cards[1].value, self.dealer.cards[0].value))



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