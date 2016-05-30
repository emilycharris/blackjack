from blackjack_player import player
from blackjack_player import dealer
from blackjack_hand import hand
from os import sys


def win_bust_hit():
    if hand.total_value == 21:
        new_game_input = print(input("You Win!  Would you like to play again? (Y)es or (N)o. ")).lower
        if new_game_input == 'y' or new_game_input == 'yes':
            game_loop()
        else:
            sys.exit()
    elif hand.total_value > 21:
        new_game_input = print(input("Sorry, you busted!  Would you like to play again? (Y)es or (N)o. ")).lower()
        if new_game_input == "y" or new_game_input == 'yes':
            game_loop()
        else:
            sys.exit()
    elif hand.total_value < 21:
        player.hit_or_stand()


def game_loop():
    hand.new_hand()
    while True:
        win_bust_hit()

game_loop()
