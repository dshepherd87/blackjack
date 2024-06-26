from player import Player
from validators import input_integer

class Blackjack:
    def game_loop():
        print("Welcome to Blackjack!")
        print()
        Blackjack.add_players()
        

    def add_players():
        players= []
        num_of_players = input_integer("Please enter the number players: ")
        for i in range(0, num_of_players):
            player_name = input(f"Enter name for player {i+1}: ")
            player_chips = input_integer(f"Enter {player_name}'s starting chips: ")
            players.append(Player(player_name, player_chips))
        print("The game will begin shortly. The players are:")
        for player in players:
            print(f"{player} with {player.get_stack()} chips")

