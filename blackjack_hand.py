from blackjack_deck import game_deck

class Hand:
    def __init__(self):
        self.value = 0
        self.card_list = []
        self.card_list_values = []

    def new_hand(self):

        while len(self.card_list) < 2:
            self.card = self.deal_card()
            self.card_value = self.card_values()
            self.card_list.append(self.card)
            self.card_list_values.append(self.card_value)

        self.total_value = sum(self.card_list_values)
        print("You were dealt the following: ", self.card_list)
        print(self.card_list_values)
        print("The value of your hand is now ", self.total_value)
        self.value += self.total_value
        return self.total_value


    def deal_card(self):
        self.face = game_deck.cards.pop(-1)
        return self.face

    def hit(self):
        self.card = self.deal_card()
        self.card_value = self.card_values()
        self.card_list.append(self.card)
        self.card_list_values.append(self.card_value)

        self.total_value = sum(self.card_list_values)
        print("You were dealt the following: ", self.card_list)
        print(self.card_list_values)
        print("The value of your hand is now ", self.total_value)
        self.value += self.total_value
        return self.total_value

    def card_values(self):
        if self.face[0] in ['1', 'J', 'Q', 'K']:
            self.value = 10
        elif self.face[0] in ['2', '3', '4', '5', '6', '7', '8', '9']:
            self.value = int(self.face[0])
        elif self.face[0] == 'A':
            self.value = 11
        return self.value


hand = Hand()
hand.new_hand()
hand.hit()
hand.hit()

