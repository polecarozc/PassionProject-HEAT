
def perfect_split(player_card, dealer_card):
    if player_card in [1, 8]:
        return 1
    elif player_card == 9 and dealer_card in [2,3,4,5,6,8,9]:
        return 1
    elif player_card == 7 and dealer_card in [2,3,4,5,6,7]:
        return 1
    elif player_card == 6 and dealer_card in [3,4,5,6]:
        return 1
    elif player_card in [2,3] and dealer_card in [4,5,6,7]:
        return 1
    else:
        return 2

def hard_total(player_total):
    pass
