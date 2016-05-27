import random


class Deck:

    def __init__(self):
        self.suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        self.numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [(number + " of " + suit) for suit in self.suits for number in self.numbers]
        random.shuffle(self.cards)

game_deck = Deck()
#print(game_deck.cards)
