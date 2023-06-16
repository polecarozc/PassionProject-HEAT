def perfect_split(player_card, dealer_card):
    if player_card in [1, 8]:
        return 1
    elif player_card == 9 and dealer_card in [2, 3, 4, 5, 6, 8, 9]:
        return 1
    elif player_card == 7 and dealer_card in [2, 3, 4, 5, 6, 7]:
        return 1
    elif player_card == 6 and dealer_card in [3, 4, 5, 6]:
        return 1
    elif player_card in [2, 3] and dealer_card in [4, 5, 6, 7]:
        return 1
    else:
        return 2


def hard_total(player_total, dealer_card):
    # stand
    if player_total > 17:
        return 1
    elif player_total in [13, 14, 15, 16] and dealer_card <= 6:
        return 1
    elif player_total == 12 and dealer_card in [4, 5, 6]:
        return 1
    # hit
    elif player_total in [13, 14, 15, 16] and dealer_card >= 6:
        return 2
    elif player_total == 12 and dealer_card in [2, 3, 7, 8, 9, 10, 11]:
        return 2
    elif player_total == 10 and dealer_card >= 10:
        return 2
    elif player_total == 9 and dealer_card in [2, 7, 8, 9, 10, 11]:
        return 2
    elif player_total == 8:
        return 2
    # double
    elif player_total == 11:
        return 3
    elif player_total == 10 and dealer_card >= 10:
        return 3
    elif player_total == 9 and dealer_card in [3, 4, 5, 6]:
        return 3
