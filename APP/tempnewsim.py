from gamelogic import game_logic
from players import player
from decks import deck
class tempnewsim:
    def __init__(self):
        self.game_logic = game_logic()
        self.decks = deck()
        self.decks.create_deck()
        self.player = player(False, self.decks)
        self.dealer = player(True, self.decks)
    def game(self):
        outcome = self.game_logic.check_blackjack()
        if outcome == 1 or 2 or 3:
            return
        outcome = self.game_logic.next_move()
        if outcome == 1 or 2:
            return
        outcome = self.game_logic.dealers_move()
        if outcome == 1:
            return


tempnewsim = tempnewsim()
tempnewsim.game()