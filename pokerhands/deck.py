import random

from .suit import Suit
from .rank import Rank
from .card import Card


class Deck:
    def __init__(self):
        self._cards = []
        for suit in Suit:
            for rank in Rank:
                self._cards.append(Card(rank, suit))
        random.shuffle(self._cards)

    def number_of_cards(self):
        return len(self._cards)

    def pick(self, number_of_cards):
        raise NotImplementedError("You need to implement this")


class NotEnoughCardsException(Exception):
    def __init__(self, message):
        super().__init__(message)


