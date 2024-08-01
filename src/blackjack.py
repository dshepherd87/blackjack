import time
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
            player_chips = input_integer(f"Enter {player_name}'s starting chips: $")
            players.append(Player(player_name, player_chips))
        print("The game will begin shortly. The players are:")
        for player in players:
            print(f"{player} with {player.get_stack()} chips")
        
        return players
    
    def place_bets(players):
        print("Place your bets please.")
        for player in players:
            while True:
                bet_amount = input_integer(f"{player}, place your bet: $")
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

    def display_table(dealer, players):
        dealer.display_dealer()
        dealer.print_first_card()
        print()
        for player in players:
            player.display_player()

    def game_round(players):
        dealer = Dealer()
        print("The dealer is shuffling the deck...")
        dealer.shuffle_deck()
        time.sleep(2)
        print()
        Blackjack.place_bets(players)
        print()
        Blackjack.deal_cards(dealer, players)
        print()
        Blackjack.display_table(dealer, players)
        print()
        for player in players:
            round = 1
            while True:
                player_action = player.turn(round)
                # if the player doubles down, double their bet then deal one more card
                if player_action == 'd':
                    player.place_bet(player.get_bet_stack())
                    player.receive_card(dealer.deal_card())
                    player.display_player()
                    if player.get_hand().get_hand_value() == 21:
                        print("21!")
                        print()
                        break
                    if player.get_hand().get_hand_value() > 21:
                        print("Bust!")
                        print()
                        player.update_bet_stack(0)
                    break
                # if the player stands, nothing to do; move on to the next player
                elif player_action == 's':
                    player.display_player()
                    break
                # if the player hits, deal one card
                elif player_action == 'h':
                    player.receive_card(dealer.deal_card())
                    player.display_player()
                    # if the player hand is now worth 21 points, stop dealing cards and continue to the next player
                    if player.get_hand().get_hand_value() == 21:
                        print("21!")
                        print()
                        break
                    # if the player hand goes over 21, they bust. stop dealing cards and take away their bet stack
                    if player.get_hand().get_hand_value() > 21:
                        print("Bust!")
                        print()
                        player.update_bet_stack(0)
                        break
                    round = round + 1
        print("Now showing the dealer's hand:")
        while True:
            dealer_hand_value = dealer.show_hand().get_hand_value()
            dealer.display_dealer()
            dealer.print_full_hand()
            print()
            
            print(f"Current value of the dealer's hand is: {dealer_hand_value}")
            print()
            # if the dealer has over 21, the house busts
            if dealer_hand_value > 21:
                print("The dealer busts!")
                for player in players:
                    if player.get_bet_stack() != 0:
                        print(f"{player} beats the dealer and wins ${player.get_bet_stack() * 2}")
                        player.give_chips(player.get_bet_stack() * 2)
                        player.update_bet_stack(0)
                break
            # if the dealer has a score of 17 or more, the house stands
            elif dealer_hand_value > 16:
                # for each player that has not already busted
                for player in players:                    
                    if player.get_bet_stack() != 0:
                        player_hand_value = player.get_hand().get_hand_value()
                        # if both the player and the dealer have the same score, then the player "pushes" and gets their bet back without penalty
                        if player_hand_value == dealer_hand_value:
                            print(f"{player} pushes")
                            player.give_chips(player.get_bet_stack())
                            player.update_bet_stack(0)
                        # if the player has a higher score than the dealer, then they win
                        elif player_hand_value > dealer_hand_value:
                            print(f"{player} beats the dealer with a score of {player_hand_value} to the dealer's {dealer_hand_value}")
                            print(f"{player} wins ${player.get_bet_stack() * 2}")
                            player.give_chips(player.get_bet_stack() * 2)
                            player.update_bet_stack(0)
                        # if the player has a lower score than the dealer, then they lose
                        else:
                            print(f"{player} loses with a score of {player_hand_value} to the dealer's {dealer_hand_value}")
                            print(f"{player} loses ${player.get_bet_stack()}")
                            player.update_bet_stack(0)
                break
            # if the dealer's hand is worth less than 17 points, they take another card
            else:
                dealer.receive_card(dealer.deal_card())
                print(f"Dealer score is {dealer_hand_value}. Dealing the next card:")
                time.sleep(3)

        




