from random import shuffle


class Player:
    """
    class for gambler
    PROPERTIES
    ----------
    money : money available to gamble with
    hand : current hand for current game
    hand_num_values : list of cards' numerical values for card in hand
    hand_value : total value of hand
    ----------
    METHODS
    clear_hand : clears hand to start a new game
    """
    def __init__(self, money):
        self.money = money
        self.hand = []
        self.hand_num_values = []
        self.hand_value = 0

    def clear_hand(self):
        self.hand = []
        self.hand_num_values = []
        self.hand_value = 0


class Card:
    """
    Represents each card in suit
    PROPERTIES
    ------------
    value : value given on card
    num_value : numerical value, 1-10 1/11 for Aces
    hidden : True if card is face down, False if face up, default False
    """
    def __init__(self, value, suit, hidden=False):
        self.value = value
        self.suit = suit
        self.hidden = hidden

        if value in ["J", "K", "Q"]:
            self.num_value = 10
        elif value == "A":
            self.num_value = 11
        else:
            self.num_value = value

    def __repr__(self):
        return str(self.value) + " of " + str(self.suit)


class House:
    """
    Represents dealer / house who is playing the game
    PROPERTIES
    ----------
    decks : number of decks cards are drawn from
    shoe : list of cards in shoe
    hand : list of cards in hand for current game
    hand_num_values : list of numerical values for card in hand
    hand_value : Total numerical value of hand
    ----------
    METHODS
    clear_hand : gets rid of hand to start new game
    new_shoe : shoe is reset
    """
    def __init__(self, decks):

        self.decks = decks

        self.shoe = []
        for x in range(0, self.decks):
            for s in ["Spades", "Diamonds", "Clubs", "Hearts"]:
                for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                    self.shoe.append(Card(v, s))
        shuffle(self.shoe)
        self.hand = []
        self.hand_num_values = []
        self.hand_value = 0

    def clear_hand(self):
        self.hand = []
        self.hand_num_values = []
        self.hand_value = 0

    def new_shoe(self):
        self.shoe = []
        for x in range(0, self.decks):
            for s in ["Spades", "Diamonds", "Clubs", "Hearts"]:
                for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                    self.shoe.append(Card(v, s))
        shuffle(self.shoe)


class Game:
    """
    class for Current Game
    PROPERTIES
    ----------
    shoe : current shoe being used
    player : gambler
    house : dealer / casino
    main_bet : value of bet placed on main game
    insurance : odds for insurance
    insurance_bet : value of bet placed on insurance by player
    -----------
    METHODS
    player_draw : player draws a card
    house_draw : house draws a card
    view_game : presents overview of game (mainly for testing purposes)
    start_game : game begins
    """

    def __init__(self, decks, player, house, bet_value, insurance_bet=1, insurance=0):
        self.shoe = []
        self.player = player
        self.house = house
        self.main_bet = bet_value
        self.insurance = insurance
        self.insurance_bet = insurance_bet
        self.over = 0 # is current game finished?
        for x in range(0, decks):
            for s in ["Spades", "Diamonds", "Clubs", "Hearts"]:
                for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                    self.shoe.append(Card(v, s))

    def player_draw(self):
        player_card = self.house.shoe.pop()
        self.player.hand.append(player_card)
        self.player.hand_num_values.append(player_card.num_value)
        self.player.hand_value += player_card.num_value

    def house_draw(self, hidden=False):
        house_card = self.house.shoe.pop()
        house_card.hidden = hidden
        self.house.hand.append(house_card)
        self.house.hand_num_values.append(house_card.num_value)
        self.house.hand_value += house_card.num_value

    def view_game(self):
        print("House Hand: ")
        print(self.house.hand)
        print()
        print("User Hand: ")
        print(self.player.hand)
        print()

    def start_game(self):

        self.player.clear_hand()
        self.house.clear_hand()

        self.over = 0

        self.player.money -= self.main_bet

        # begin game
        self.player_draw()
        self.house_draw()

        self.player_draw()
        self.house_draw()

        if self.house.hand_value == 21 and self.player.hand_value != 21:
            self.over = 1 # player loses
        elif self.house.hand_value == 21 and self.player.hand_value == 21:
            self.player.money += self.main_bet # player regains initial bet
            self.over = 1
        elif self.house.hand_value != 21 and self.player.hand_value == 21:
            self.player.money += 2 * self.main_bet # 2 is placeholder for blackjack odds CHANGE LATER
            self.over = 1
        else:
            pass

        if self.over == 0 and self.player.hand_value < 21:
            #IMPLEMENT STRATEGY FOR PLAYER
            while self.house.hand_value < 17:
                self.house_draw()
        # self.view_game()

        # implement insurance


        # if self.house.hand_num_values[0] == 11 and self.insurance == 1:
        #     self.player.money -= self.insurance_bet
        #     if self.house.hand_num_values[1] == 10:
        #         self.player.money += 3 * self.insurance_bet
        #
        # if self.player.hand_value == 21 and self.house.hand_value == 21:
        #     self.over = 1
        # elif self.player.hand_value == 21:
        #     self.over = 1
        # elif self.house.hand_value == 21:
        #     self.over = 1
        # else:
        #     pass
        #
        # if self.over == 0:
        #     while self.player.hand_value < 17:  # change to incorporate card counting
        #         self.player_draw()
        #
        #         while 11 in self.player.hand_num_values and self.player.hand_value > 21:
        #             self.player.hand_num_values.remove(11)
        #             self.player.hand_num_values.append(1)
        #             self.player.hand_value = sum(self.player.hand_num_values)
        #
        # if self.over == 0 and self.player.hand_value <= 21:
        #     while self.house.hand_value <= 17:
        #         self.house_draw()
        #
        #     while 11 in self.house.hand_num_values and self.house.hand_value > 21:
        #         self.house.hand_num_values.remove(11)
        #         self.house.hand_num_values.append(1)
        #         self.house.hand_value = sum(self.house.hand_num_values)
        #
        # # add blackjack conditions here
        # if self.house.hand_value == 21 and self.player.hand_value == 21:
        #     self.player.money += self.main_bet
        # elif self.player.hand_value == 21 and len(self.player.hand) == 2:
        #     self.player.money += 2.5 * self.main_bet
        # elif self.player.hand_value == 21:
        #     self.player.money += 2 * self.main_bet
        # elif (self.player.hand_value > self.house.hand_value) and self.player.hand_value < 21:
        #     self.player.money += 2 * self.main_bet
        # elif (self.player.hand_value <= 21) and (self.house.hand_value > 21):
        #     self.player.money += 2 * self.main_bet
        # elif self.player.hand_value == self.house.hand_value and self.player.hand_value < 21:
        #     self.player.money += self.main_bet

        # tests
        # self.view_game()
        # print(self.over)
        # print(self.player.money)
