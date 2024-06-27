from player import Player
from dealer import Dealer
from validators import input_integer, input_string

class Blackjack:
    def game_loop():
        print("Welcome to Blackjack!")
        print()
        players = Blackjack.add_players()
        Blackjack.game_round(players)
        

    def add_players():
        players= []
        num_of_players = input_integer("Please enter the number players: ")
        for i in range(0, num_of_players):
            player_name = input_string(f"Enter name for player {i+1}: ")
            player_chips = input_integer(f"Enter {player_name}'s starting chips: ")
            players.append(Player(player_name, player_chips))
        print("The game will begin shortly. The players are:")
        for player in players:
            print(f"{player} with {player.get_stack()} chips")
        
        return players
    
    def place_bets(players):
        print("Place your bets please.")
        for player in players:
            while True:
                bet_amount = input_integer(f"{player}, place your bet: ")
                try:
                    player.place_bet(bet_amount)
                    break
                except Exception as e:
                    print(e)

    def deal_cards(dealer, players):
        print("The cards are beind dealt...")
        print()
        # deal the first round of cards
        for player in players:
            player.receive_card(dealer.deal_card())
            print(f"{player} receives the {player.get_hand().show_card(0)}")
        dealer.receive_card(dealer.deal_card())
        print(f"The dealer receives the {dealer.show_hand().show_card(0)}")
        # deal the second round of cards
        for player in players:
            player.receive_card(dealer.deal_card())
            print(f"{player} receives the {player.get_hand().show_card(1)}")
        dealer.receive_card(dealer.deal_card())



    def game_round(players):
        dealer = Dealer()
        print("The dealer is shuffling the deck...")
        dealer.shuffle_deck()
        print()
        Blackjack.place_bets(players)
        print()
        Blackjack.deal_cards(dealer, players)

        




