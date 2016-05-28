from blackjack_player import player
from blackjack_player import dealer
from blackjack_hand import hand
from os import sys


class Game:
    def __init__(self):
        self.player = player
        self.dealer = dealer
        self.new_game_input = ''
        #print("Welcome to Blackjack!")

    def win_or_bust(self):
        if player.hand.total_value == 21:
            self.new_game_input = print(input("You Win!  Would you like to play again? (Y)es or (N)o. ")).lower
            if self.new_game_input == 'y' or self.new_game_input == 'yes':
                self.game_loop()
            else:
                sys.exit()
        if player.hand.total_value > 21:
            self.new_game_input = print(input("Sorry, you busted!  Would you like to play again? (Y)es or (N)o. ")).lower()
            if self.new_game_input == "y" or self.new_game_input == 'yes':
                self.game_loop()
            else:
                sys.exit()
        else:
            player.hit_or_stand()




    def game_loop(self):
        player.new_hand()
        player.hit_or_stand()
        player.game.win_or_bust()

game = Game()

