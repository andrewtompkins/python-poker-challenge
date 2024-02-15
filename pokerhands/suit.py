from enum import Enum
from functools import total_ordering


@total_ordering
class Suit(Enum):
    SPADES = 0
    HEARTS = 1
    CLUBS = 2
    DIAMONDS = 3

    def __str__(self):
        return self.name.lower()

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return isinstance(other, Suit) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def compare_to(self, other):
        return self.value - other.value
