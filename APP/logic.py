
def set_shuffler():
    shuffler = input('Please select the type of shuffler: ')
    if shuffler.lower() == 'manual':
        return 1
    elif shuffler.lower() == 'automatic':
        return 2
    elif shuffler.lower() == 'continuous':
        return 3
    else:
        print('I did not understand that, please put in a valid shuffler. \n')
        print('There are 3 kinds of shuffling:\n-------- \nManual.\nAutomatic.\nContinuous.\n--------')
        set_shuffler()

def shoe_size():
    return int(input('Please enter shoe size: '))

def set_decks():
    return int(input('Please set the amount of decks you will be playing with: '))

def set_simulations():
    return int(input('Lastly, please set the amount of simulations you would like to run: '))

def run_simulation():
    shuffler = set_shuffler()
    decks = set_decks()
    shoe = shoe_size()
    simulations = set_simulations()
    

