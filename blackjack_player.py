from blackjack_hand import player_hand
from blackjack_hand import dealer_hand
from os import sys


class Player:
    def __init__(self):
        self.player_decision = ""
        self.new_game_input = ''

    def hit_or_stand(self):
        self.player_decision = input("Would you like to (h)it or (s)tand? ").lower()
        if self.player_decision == 'h' or 'hit':
            player_hand.hit()
            print("Your hand includes the following cards: {}".format(player_hand.card_list))
            print("The value of your hand is now {}.".format(player_hand.total_value))
        if self.player_decision == 's' or 'stand':
            dealer.hit_or_stand()
        return self.player_decision

    def win_bust_hit(self):
        if player_hand.total_value == 21:
            new_game_input = input("You Win!  Would you like to play again? (Y)es or (N)o. ").lower()
            if new_game_input == 'y' or new_game_input == 'yes':
                self.game_loop()
            else:
                sys.exit()
        elif player_hand.total_value > 21:
            new_game_input = input("Sorry, you busted!  Would you like to play again? (Y)es or (N)o. ").lower()
            if new_game_input == "y" or new_game_input == 'yes':
                self.game_loop()
            else:
                sys.exit()
        else:
            player.hit_or_stand()

    def game_loop(self):
        player_hand.clear_hand()
        dealer_hand.clear_hand()
        player_hand.new_hand()
        dealer_hand.new_hand()
        print("Your hand includes the following cards: {}.".format(player_hand.card_list))
        print("The value of your hand is {}.".format(player_hand.total_value))
        print("The dealer's hand shows the {}.".format(dealer_hand.card_list[0]))
        while True:
            self.win_bust_hit()
        else:
            dealer.hit_or_stand()

class Dealer(Player):
    def hit_or_stand(self):
        while True:
            if dealer_hand.total_value < 17:
                print("The dealer will hit.")
                dealer_hand.hit()
                #print("The value of the dealer's hand is {}.".format(dealer_hand.total_value))
        else:
            print("The dealer will stand.")
            if player_hand.total_value > dealer_hand.total_value:
                print("You Win! Your hand's value was {} "
                        "and the dealer's was {}.".format(player_hand.total_value, dealer_hand.total_value))
                new_game_input = input("Would you like to play again? (Y)es or (N)o. ").lower()
                if new_game_input == 'y' or new_game_input == 'yes':
                    self.game_loop()
                else:
                    sys.exit()
            elif dealer_hand.total_value > player_hand.total_value:
                new_game_input = input("You lost!  Would you like to play again? (Y)es or (N)o. ").lower()
                if new_game_input == 'y' or new_game_input == 'yes':
                    self.game_loop()
                else:
                    sys.exit()



player = Player()
dealer = Dealer()

player.game_loop()



