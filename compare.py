import deck
import card


def deal_cards(my_deck):
    comp_deck = []
    for x in range(5):
        comp_deck.append(my_deck.deal())
    return comp_deck


def main():
    my_deck = deck.Deck()
    my_deck.shuffle()
    player_1 = deal_cards(my_deck)
    player_2 = deal_cards(my_deck)
