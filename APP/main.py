from blackjacksim import game
from logic import logic


if __name__=='__main__':
    logic = logic()
    bankroll = logic.bankroll()
    minbet = logic.minbet()
    blackjack = game(bankroll, logic.shoe_size(), minbet, logic.maxbet(), logic.set_shuffler())
    while blackjack.play() != 10:
        print('--------COMPLETED__RUN--------')
    print('you went broke!!!!')