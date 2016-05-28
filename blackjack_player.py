from blackjack_hand import hand


class Player:
    def __init__(self):
        self.hand_value = 0
        self.player_decision = ""

    def hit_or_stand(self):
        print("The value of your hand is currently {}.".format(hand.total_value))
        self.player_decision = input("Would you like to (h)it or (s)tand? ").lower()
        if self.player_decision == 'h' or 'hit':
            hand.hit()
            print("You were dealt the following: ", hand.card_list)
            print(hand.card_list_values)
            print("The value of your hand is now ", hand.total_value)
        return self.player_decision


class Dealer(Player):
    def hit_or_stand(self):
        print("The value of the dealer's hand is {}.".format(hand.total_value))
        if hand.total_value < 17:
            print("The dealer will hit.")
            hand.hit()
        else:
            print("The dealer will stand.")

player = Player()
player.hit_or_stand()
dealer = Dealer()