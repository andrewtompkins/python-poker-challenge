import random
from .suit import Suit
from .rank import Rank
from .card import Card

class Deck:

    def __init__(self):
        self.initial_deck_size = 52
        self.number_of_cards_left = self.initial_deck_size;
        self._cards = []
        for suit in Suit:
            for rank in Rank:
                self._cards.append(Card(rank, suit))
        random.shuffle(self._cards)

    def number_of_cards(self):
        return self.number_of_cards_left
    
    def get_initial_deck_size(self):
        return self.initial_deck_size

    def pick(self, number_of_cards):
        if number_of_cards > self.number_of_cards_left:
            raise NotEnoughCardsException("There are not enough cards in the deck. The Deck contains " + str(self.number_of_cards_left) + " and " + str(number_of_cards) + " were requested")
        else:
            picked_cards = self._cards[:min(number_of_cards, len(self._cards))]
            self.number_of_cards_left -= len(picked_cards)
            return picked_cards

class NotEnoughCardsException(Exception):
    def __init__(self, message):
        super().__init__(message)

