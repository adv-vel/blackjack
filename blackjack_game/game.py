from random import shuffle

class Player:

    def __init__(self, money):
        self.money = money
        self.bet_value = 0
        self.insurance_bet_value = 0
        self.ace_value = 11

        self.hand = []
        self.hand_value = 0

    def place_bet(self):
        self.bet_value = input("How much would you like to place: ")
        self.money = self.money - self.bet_value

    def payout(self, odds, bet_type):
        if bet_type == "main":
            self.money += odds*self.bet_value
        elif bet_type == "insurance":
            self.money += odds*self.insurance_bet_value
        else:
            self.money += odds*self.insurance_bet_value

    def set_ace_value(self, value):
        self.ace_value = value
        self.hand_value = 0
        for card in self.hand:
            if card.value == "A":
                card.num_value = value
                self.hand_value += value
            else:
                self.hand_value += card.num_value
            

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

class Game:

    def __init__(self, decks, player, blackjack_odds):
        self.shoe = []
        self.player = player
        self.house_hand = []
        self.house_hand_value = 0
        self.blackjack_odds = blackjack_odds
        self.main_bet = 0
        for x in range(0, decks):
            for s in ["Spades", "Diamonds", "Clubs", "Hearts"]:
                for v in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                    self.shoe.append(Card(v, s))

    def shoe_shuffle(self):
        shuffle(self.shoe)
        
    def player_draw(self):
        player_card = self.shoe.pop()
        self.player.hand.append(player_card)

    def house_draw(self):
        house_card = self.shoe.pop()
        self.house_hand.append(house_card)

    def view_game(self):
        print("House Hand: ")
        print(self.house_hand)
        print()
        print("User Hand: ")
        print(self.player.hand)
        print()        

    def start_game(self):

        self.shoe_shuffle()

        self.main_bet = int(input("How much would you like to bet: "))
        self.player.money -= self.main_bet

        self.player_draw()      #face up
        self.house_draw()       #face up

        self.player_draw()      #face up
        self.house_draw()  #face down        self.house_draw(False)  #face down

        self.view_game()

        if self.player.hand_value == 21 and self.house_hand_value == 21:
            self.player.money += self.main_bet
            print("Tie!")
            print()
            return
        elif self.player.hand_value == 21:
            print("Win!")
            print()
            self.player.money += (1+self.blackjack_odds)*self.main_bet
            return

        if self.house_hand[0].value == "A":
            self.player.insurance_bet_value = int(input("Insurance bet: "))
            if self.house_hand[1].num_value == 10:
                self.house_hand[1].face_up = True
                self.player.payout(self.insurance_odds, "insurance")
                return

        option = "H"
        while self.player.hand_value < 21 or option != "S":
            option = input("Would you like to hit or stick (H/S): ")
            if option == "H":
                self.view_game()
                self.player_draw()
            elif option == "S":
                break
        
        #from this point player hand value <

        if self.player.hand_value > 21:
            print("Bust!")

        while self.house_hand_value <= 17:
            self.house_draw()
            self.view_game()
        
        if self.house_hand_value == 21:
            print("House Wins")
        elif self.house_hand_value > 21:
            print("Player wins")
            self.player.money += self.main_bet * 2.5
