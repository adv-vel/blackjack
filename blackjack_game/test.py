from blackjack_game import Card, Game, Player

me = Player(1000)
my_game = Game(6, me, 100)
my_game.start_game()