from blackjack_hand import player_hand
from blackjack_hand import dealer_hand
from os import sys


class Player:
    def __init__(self):
        self.player_decision = ""
        self.new_game_input = ''

    def hit_or_stand(self):
        self.player_decision = ''
        self.player_decision = input("Would you like to (h)it or (s)tand? ").lower()
        if self.player_decision == 's' or self.player_decision == 'stand':
            print("The player stands.  The dealer will take a turn.")
            dealer.hit_or_stand()
        elif self.player_decision == 'h' or self.player_decision == 'hit':
            player_hand.hit()
            print("Your hand now includes the following cards: {}".format(player_hand.card_list))
            print("The value of your hand is now {}.".format(player_hand.total_value))
            player.win_bust_hit()


    def win_bust_hit(self):
        if player_hand.total_value < 21:
            player.hit_or_stand()
        if player_hand.total_value == 21:
            new_game_input = input("You Win!  Would you like to play again? (Y)es or (N)o. ").lower()
            if new_game_input == 'y' or new_game_input == 'yes':
                print("\n")
                self.game_loop()
            else:
                sys.exit()
        if player_hand.total_value > 21:
            new_game_input = input("Sorry, you busted!  Would you like to play again? (Y)es or (N)o. ").lower()
            if new_game_input == "y" or new_game_input == 'yes':
                print('\n')
                self.game_loop()
            else:
                sys.exit()

    def game_loop(self):
        player_hand.clear_hand()
        dealer_hand.clear_hand()
        player_hand.new_hand()
        dealer_hand.new_hand()
        #player.hit_or_stand()
        print("Your hand includes the following cards: {}.".format(player_hand.card_list))
        print("The value of your hand is {}.".format(player_hand.total_value))
        print("The dealer's hand shows the {}.".format(dealer_hand.card_list[1]))
        while True:
            self.win_bust_hit()

class Dealer(Player):
    def hit_or_stand(self):
        while dealer_hand.total_value < 17:
                print("The dealer will hit.")
                dealer_hand.hit()
                print("The dealer shows {}.".format(dealer_hand.card_list[1:]))
        else:
            print("The dealer will stand.")
            if dealer_hand.total_value <= 21:
                if player_hand.total_value > dealer_hand.total_value:
                    print("You Win! Your hand's value was {} "
                            "and the dealer's was {}.".format(player_hand.total_value, dealer_hand.total_value))
                    new_game_input = input("Would you like to play again? (Y)es or (N)o. ").lower()
                    if new_game_input == 'y' or new_game_input == 'yes':
                        self.game_loop()
                    else:
                        sys.exit()
                elif dealer_hand.total_value > player_hand.total_value:
                    print("You lost!  The dealer's hand valued {} "
                           "and yours valued {}.".format(dealer_hand.total_value, player_hand.total_value))
                    new_game_input = input("Would you like to play again? (Y)es or (N)o. ").lower()
                    if new_game_input == 'y' or new_game_input == 'yes':
                        self.game_loop()
                    else:
                        sys.exit()
            else:
                print("The dealer busted. His cards valued {} while yours valued {}. You win!".format(dealer_hand.total_value, player_hand.total_value))
                new_game_input = input("Would you like to play again? (Y)es or (N)o. ").lower()
                if new_game_input == 'y' or new_game_input == 'yes':
                    self.game_loop()
                else:
                    sys.exit()



player = Player()
dealer = Dealer()

player.game_loop()



