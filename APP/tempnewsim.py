from gamelogic import game_logic
import time
class tempnewsim:
    def __init__(self):
        self.game_logic = game_logic(1,1,1,1,1)

    def game(self):

        player_state = self.game_logic.player.deal_cards()
        dealer_state = self.game_logic.dealer.deal_cards()

        self.game_logic.check_ace()

        if self.game_logic.check_blackjack(player_state,dealer_state) != 4:
            print('nobody got blackjack, moving onto next move')

        print('onto next move, everything worked')
        print(self.game_logic.decks.count)
        self.game_logic.player.cards.clear()
        self.game_logic.dealer.cards.clear()
        # outcome = self.game_logic.next_move()
        # if outcome == 1 or 2:
        #     return
        # outcome = self.game_logic.dealers_move()
        # if outcome == 1:
        #     return


tempnewsim = tempnewsim()
while tempnewsim.game() != 100:
    time.sleep(1)

