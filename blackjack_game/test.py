from blackjack_game import Card, Game, Player, House
def blackjack_test():
    me = Player(1000)
    for i in range(0, 10):
        casino = House(6)
        for x in range(0, 20):
            my_game = Game(6, me, casino, 10, insurance=1, insurance_bet=5)
            my_game.start_game()

            if me.money == 0:
                break

        if me.money == 0:
            print(i, x)
            break

    return me.money

profits = []

for x in range(0, 100):
    profits.append(blackjack_test() - 1000)

x_vals = [x for x in range(0, 100)]
print(sum(profits) / (100 * 200))
#calculated house edge of approx. 4.5%
