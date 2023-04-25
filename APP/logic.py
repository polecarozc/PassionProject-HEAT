class logic:
    def __init__(self):
        pass
    def set_shuffler(self):
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
            self.set_shuffler()

    def shoe_size(self):
        return int(input('Please enter shoe size: '))


    def set_decks(self):
        return int(input('Please set the amount of decks you will be playing with: '))

    def bankroll(self):
        return int(input('Set bankroll amount: '))
    def minbet(self):
        return int(input('Set the min bet: '))

    def maxbet(self):
        return int(input('set the max bet: '))
