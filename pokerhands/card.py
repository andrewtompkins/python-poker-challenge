from functools import total_ordering


@total_ordering
class Card:
    def __init__(self, rank, suit):
        if rank is None:
            raise ValueError("Rank of a Card may not be None")
        if suit is None:
            raise ValueError("Suit of a Card may not be None")
        self.rank = rank
        self.suit = suit

    def compare_to(self, other):
        return self.rank.value - other.rank.value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        if self is other:
            return True
        if self.rank != other.rank:
            return False
        return self.suit == other.suit

    def __lt__(self, other):
        return self.compare_to(other) < 0

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


