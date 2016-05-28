from blackjack_deck import game_deck

class Hand:
    def __init__(self):
        self.total_value = 0
        self.card_list = []
        self.card_list_values = []
        self.card_list_values_no_aces = []

    def new_hand(self):
            self.hit()
            self.hit()
            print("Your hand is as follows: ", hand.card_list)
            print(hand.card_list_values)
            #print("The value of your hand is now ", hand.total_value)

    def deal_card(self):
        self.face = game_deck.cards.pop(-1)
        return self.face

    def hit(self):
        self.card = self.deal_card()
        self.card_value = self.card_values()
        self.card_list.append(self.card)
        self.card_list_values.append(self.card_value)
        self.revalue_aces()
        self.total_value = sum(self.card_list_values)
        return self.total_value

    def initial_ace_values(self):
            if sum(self.card_list_values_no_aces) <= 10:
                self.value = 11
            else:
                self.value = 1
            return self.value

    def card_values(self):
        if self.face[0] in ['1', 'J', 'Q', 'K']:
            self.value = 10
            self.card_list_values_no_aces.append(self.value)
        elif self.face[0] in ['2', '3', '4', '5', '6', '7', '8', '9']:
            self.value = int(self.face[0])
            self.card_list_values_no_aces.append(self.value)
        else:
            self.initial_ace_values()
        return self.value

    def revalue_aces(self):
        for self.i, self.item in enumerate(self.card_list_values):
            if self.item == 11 or self.item == 1:
                if sum(self.card_list_values_no_aces) <= 10:
                    self.card_list_values[self.i] = 11
                else:
                    self.card_list_values[self.i] = 1
        return self.card_list_values



hand = Hand()
hand.new_hand()
