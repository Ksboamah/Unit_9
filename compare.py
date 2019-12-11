import deck
import card


def deal_cards(my_deck):
    comp_deck = []
    for x in range(5):
        comp_deck.append(my_deck.deal())
        return comp_deck


def compare_cards(player_1, player_2):
    if player_1 > player_2:
        return True
    else:
        return False


def points_saver(game_round, holder, comp_holder):
    if game_round == True:
        holder.append("point")
    else:
        comp_holder.append("point")


def determine_winner(holder, comp_holder):
    if len(holder) > len(comp_holder):
        print("Player 1 wins the game.")
    else:
        print("Player 2 wins the game.")


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    player_1 = deal_cards(my_deck)
    player_2 = deal_cards(my_deck)
    game_round = compare_cards(player_1, player_2)
    holder = []
    comp_holder = []
    points_saver(game_round, holder, comp_holder)
    determine_winner(holder, comp_holder)

main()