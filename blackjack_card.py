import random
from blackjack_deck import game_deck

values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10}
class Card:
    def __init__(self):
        for self.card in game_deck.cards:
            self.value = 0
            self.face = ""

    def evaluate_card(self):
        self.face = game_deck.cards.pop(-1)
        print("Your card is the ", self.face)
        if self.face[0] in ['1', 'J', 'Q', 'K']:
            self.value += 10
        elif card.face[0] in ['2', '3', '4', '5', '6', '7', '8', '9']:
            self.value += int(self.face[0])
        elif self.face[0] == 'A':
            self.value += 11
        return self.value

card = Card()
value = card.evaluate_card()
print("The value of your card is {}.".format(value))
print(len(game_deck.cards))
