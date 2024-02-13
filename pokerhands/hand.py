from copy import deepcopy


class Hand:
    def __init__(self, cards):
        self._cards = deepcopy(cards) if cards is not None else []

    def number_of_cards(self):
        return len(self._cards)

    def describe_hand_rank(self):
        raise NotImplementedError("You need to implement this")

    def compare_to(self, other):
        raise NotImplementedError("You need to implement this")
