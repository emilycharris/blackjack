import random
from blackjack_deck import game_deck

values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'J':10, 'Q':10, 'K':10}
class Card:
    def __init__(self):
        for self.card in game_deck.cards:
            self.value = 0
            self.face = ""

    def draw_card(self):
        self.face = game_deck.cards.pop(-1)
        print("Your card is the " + self.face)
        print("The value of your card is {}.".format(card.card_value()))

    def card_value(self):
        if self.face[0] in ['J', 'Q', 'K']:
            self.value += 10
        elif self.face[0] in ['2', '3', '4', '5', '6', '7', '8', '9']:
            self.value += int(self.face[0])


card = Card()
card.draw_card()
card.card_value()
print(len(game_deck.cards))
card.draw_card()
print(len(game_deck.cards))