from enum import Enum
from functools import total_ordering


@total_ordering
class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4

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
