from blackjacksim import game
from logic import logic


if __name__=='__main__':
    logic = logic()
    bankroll = logic.bankroll()
    minbet = logic.minbet()
    blackjack = game(bankroll, logic.shoe_size(), minbet, logic.maxbet(), logic.set_shuffler())
    while bankroll > minbet:
        blackjack.play()
        print('--------COMPLETED__RUN--------')
    print('you went broke!!!!')