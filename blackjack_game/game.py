from random import shuffle


class Player:

    def __init__(self, money):
        self.money = money

        self.hand = []
        self.hand_num_values = []
        self.hand_value = 0

    def place_bet(self, bet_value):
        self.bet_value = bet_value
        self.money = self.money - self.bet_value

    def payout(self, odds, bet_type):
        if bet_type == "main":
            self.money += odds * self.bet_value
        elif bet_type == "insurance":
            self.money += odds * self.insurance_bet_value
        else:
            self.money += odds * self.insurance_bet_value
class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        if value in ["J", "K", "Q"]:
            self.num_value = 10
        elif value == "A":
            self.num_value = 11
        else:
            self.num_value = value

    def __repr__(self):
        return str(self.value) + " of " + str(self.suit)

class House:
    def __init__(self, suits):

        self.shoe = []
        for x in range(0, decks):
            for s in ["Spades", "Diamonds", "Clubs", "Hearts"]:
                for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                    self.shoe.append(Card(v, s))


class Game:

    def __init__(self, decks, player, bet_value):
        self.shoe = []
        self.player = player
        self.house_hand = []
        self.house_hand_value = 0
        self.house_hand_num_values = []
        self.main_bet = bet_value
        for x in range(0, decks):
            for s in ["Spades", "Diamonds", "Clubs", "Hearts"]:
                for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                    self.shoe.append(Card(v, s))

    def shoe_shuffle(self):
        shuffle(self.shoe)

    def player_draw(self):
        player_card = self.shoe.pop()
        self.player.hand.append(player_card)
        self.player.hand_num_values.append(player_card.num_value)
        self.player.hand_value += player_card.num_value

    def house_draw(self):
        house_card = self.shoe.pop()
        self.house_hand.append(house_card)
        self.house_hand_num_values.append(house_card.num_value)
        self.house_hand_value += house_card.num_value

    def view_game(self):
        print("House Hand: ")
        print(self.house_hand)
        print()
        print("User Hand: ")
        print(self.player.hand)
        print()

    def start_game(self):
        self.over = 0

        self.shoe_shuffle()

        self.player.money -= self.main_bet

        # begin game
        self.player_draw()
        self.house_draw()

        self.player_draw()
        self.house_draw()

        self.view_game()

        if self.player.hand_value == 21 and self.house_hand_value == 21:
            self.over = 1
            self.player.money += self.main_bet
        elif self.player.hand_value == 21:
            self.over = 1
            self.player.money += 2.5 * self.main_bet
        else:
            pass

        def check_game():

            while 11 in self.player.hand_num_values and self.player.hand_value > 21:
                self.player.hand_num_values.remove(11)
                self.player.hand_num_values.append(1)
                self.player.hand_value = sum(self.player.hand_num_values)

            while 11 in self.house_hand_num_values and self.house_hand_value > 21:
                self.house_hand_num_values.remove(11)
                self.house_hand_num_values.append(1)
                self.house_hand_value = sum(self.house_hand_num_values)

            if self.player.hand_value >= 21:
                self.over = 1

            if self.house_hand_value >= 21:
                self.over = 1

        while self.over == 0:
            option = 0
            #option = input("Hit or Stick (H/S): ")
            if self.player.hand_value < 17:
                option = "H"
            else:
                option = "S"

            if option == "S":
                break

            elif option == "H":
                self.player_draw()
                if self.house_hand_value <= 17:
                    self.house_draw()

            check_game()

            self.view_game()

        while self.house_hand_value <= 17:
            self.house_draw()

        if self.player.hand_value > 21:
            pass
        elif self.house_hand_value > 21:
            self.player.money += 2.5 * self.main_bet
        elif self.player.hand_value == self.house_hand_value:
            self.player.money += self.main_bet
        elif self.player.hand_value > self.house_hand_value:
            self.player.money += 2 * self.main_bet
        elif self.house_hand_value > self.player.hand_value:
            pass
        else:
            pass
