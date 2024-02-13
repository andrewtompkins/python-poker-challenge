from abc import ABC, abstractmethod


class HandRank(ABC):
    def __init__(self, hand_strength):
        self._hand_strength = hand_strength

    def compare_to(self, other):
        strength = self._hand_strength.compare_to(other.get_hand_strength())
        if strength == 0:
            strength = self.compare_same_rank(other)
        return strength

    def get_hand_strength(self):
        return self._hand_strength

    @abstractmethod
    def compare_same_rank(self, other):
        pass

    @abstractmethod
    def describe_hand(self):
        pass
