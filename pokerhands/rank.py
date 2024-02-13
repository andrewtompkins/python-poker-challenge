from enum import Enum
from functools import total_ordering


@total_ordering
class Rank(Enum):
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

    def __str__(self):
        return self.name.lower()

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return isinstance(other, Rank) and self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def compare_to(self, other):
        return self.value - other.value

