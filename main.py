import enum
import random


class Card(enum.IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(enum.Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMOND = 'diamonds'


class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit


def main():
    # Lists
    full_deck = []

    def create_deck():
        for suit in Suit:
            for card in Card:
                full_deck.append(PlayingCard(Card(card), Suit(suit)))
        return full_deck

    create_deck()
    print(full_deck[1])


if __name__ == '__main__':
    main()
