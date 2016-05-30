from blackjack_hand import hand
from os import sys


class Player:
    def __init__(self):
        self.player_decision = ""
        self.new_game_input = ''

    def hit_or_stand(self):
        self.player_decision = input("Would you like to (h)it or (s)tand? ").lower()
        if self.player_decision == 'h' or 'hit':
            hand.hit()
            print("Your hand includes the following cards: {}".format(hand.card_list))
            print("The value of your hand is now {}.".format(hand.total_value))
        return self.player_decision

    def win_bust_hit(self):
        if hand.total_value == 21:
            new_game_input = input("You Win!  Would you like to play again? (Y)es or (N)o. ").lower()
            if new_game_input == 'y' or new_game_input == 'yes':
                self.game_loop()
            else:
                sys.exit()
        elif hand.total_value > 21:
            new_game_input = input("Sorry, you busted!  Would you like to play again? (Y)es or (N)o. ").lower()
            if new_game_input == "y" or new_game_input == 'yes':
                self.game_loop()
            else:
                sys.exit()
        elif hand.total_value < 21:
            player.hit_or_stand()

    def game_loop(self):
        hand.clear_hand()
        hand.new_hand()
        print("Your hand includes the following cards: {}.".format(hand.card_list))
        print("The value of your hand is {}.".format(hand.total_value))
        while True:
            self.win_bust_hit()

class Dealer(Player):
    def hit_or_stand(self):
        print("The value of the dealer's hand is {}.".format(hand.total_value))
        if hand.total_value < 17:
            print("The dealer will hit.")
            hand.hit()
        else:
            print("The dealer will stand.")




player = Player()
dealer = Dealer()

player.game_loop()



