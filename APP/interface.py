from logic import logic
logic = logic()
class interface:

    def __init__(self):
        self.logic = logic()

    def set_logic(self):
        self.logic.set_decks()
        self.logic.shoe_size()




