from .hand_rank import HandRank
from .hand_strength import HandStrength


class HighCard(HandRank):
    def __init__(self, cards):
        super().__init__(HandStrength.HI_CARD)
        if cards is None or not isinstance(cards, list) or len(cards) != 5:
            raise ValueError("cards must be set to a list of 5 cards")
        self.cards = cards
        self.cards.sort(reverse=True)

    def compare_same_rank(self, other):
        for card_index in range(0, len(self.cards)):
            card_comparison = self.cards[card_index].compare_to(other.cards[card_index])
            if card_comparison != 0:
                return card_comparison

        return 0

    def describe_hand(self):
        return "High card {}".format(self.cards[0])


class OnePair(HandRank):
    def __init__(self, pair, rest):
        super().__init__(HandStrength.ONE_PAIR)
        if pair is None:
            raise ValueError("pair must be set")
        if rest is None or not isinstance(rest, list) or len(rest) != 3:
            raise ValueError("rest must be set to a list of 3 kickers")
        self.pair = pair
        self.rest = rest
        self.rest.sort(reverse=True)

    def compare_same_rank(self, other):
        pair_comparison = self.pair.compare_to(other.pair)
        if pair_comparison != 0:
            return pair_comparison
        for rest_index in range(0, len(self.rest)):
            kicker_comparison = self.rest[rest_index].compare_to(other.rest[rest_index])
            if kicker_comparison != 0:
                return kicker_comparison

        return 0

    def describe_hand(self):
        return "One pair of {}s".format(self.pair)


class TwoPair(HandRank):
    def __init__(self, high_pair, low_pair, kicker):
        super().__init__(HandStrength.TWO_PAIR)
        if high_pair is None:
            raise ValueError("high_pair must be set")
        if low_pair is None:
            raise ValueError("low_pair must be set")
        if kicker is None:
            raise ValueError("kicker must be set")
        self.high_pair = high_pair
        self.low_pair = low_pair
        self.kicker = kicker

    def compare_same_rank(self, other):
        high_pair_score = self.high_pair.compare_to(other.high_pair)
        if high_pair_score != 0:
            return high_pair_score
        low_pair_score = self.low_pair.compare_to(other.low_pair)
        if low_pair_score != 0:
            return low_pair_score
        return self.kicker.compare_to(other.kicker)

    def describe_hand(self):
        return "Two pair, {}s and {}s".format(self.high_pair, self.low_pair)


class ThreeOfAKind(HandRank):
    def __init__(self, card_rank):
        super().__init__(HandStrength.THREE_OF_A_KIND)
        if card_rank is None:
            raise ValueError("card_rank must be set")
        self.card_rank = card_rank

    def compare_same_rank(self, other):
        return self.card_rank.compare_to(other.card_rank)

    def describe_hand(self):
        return "Three of a kind of {}s".format(self.card_rank)


class Straight(HandRank):
    def __init__(self, high_card_rank):
        super().__init__(HandStrength.STRAIGHT)
        if high_card_rank is None:
            raise ValueError("high_card_rank must be set")
        self.high_card_rank = high_card_rank

    def compare_same_rank(self, other):
        return self.high_card_rank.compare_to(other.high_card_rank)

    def describe_hand(self):
        return "Straight, {} high".format(self.high_card_rank)


class Flush(HandRank):
    def __init__(self, cards):
        super().__init__(HandStrength.FLUSH)
        if cards is None or not isinstance(cards, list) or len(cards) != 5:
            raise ValueError("cards must be set to a list of 5 cards")
        self.cards = cards
        self.cards.sort(reverse=True)

    def compare_same_rank(self, other):
        for card_index in range(0, len(self.cards)):
            card_comparison = self.cards[card_index].compare_to(other.cards[card_index])
            if card_comparison != 0:
                return card_comparison

        return 0

    def describe_hand(self):
        return "Flush, {} high".format(self.cards[0].rank)


class FullHouse(HandRank):
    def __init__(self, trips, pair):
        super().__init__(HandStrength.FULL_HOUSE)
        if trips is None:
            raise ValueError("trips must be set")
        if pair is None:
            raise ValueError("pair must be set")
        self.trips = trips
        self.pair = pair

    def compare_same_rank(self, other):
        trips_comparison = self.trips.compare_to(other.trips)
        if trips_comparison != 0:
            return trips_comparison
        return self.pair.compare_to(other.pair)

    def describe_hand(self):
        return "Full house, {}s over {}s".format(self.trips, self.pair)


class FourOfAKind(HandRank):
    def __init__(self, card_rank):
        super().__init__(HandStrength.FOUR_AS_A_KIND)
        if card_rank is None:
            raise ValueError("card_rank must be set")
        self.card_rank = card_rank

    def compare_same_rank(self, other):
        return self.card_rank.compare_to(other.card_rank)

    def describe_hand(self):
        return "Four of a kind of {}s".format(self.card_rank)


class StraightFlush(HandRank):
    def __init__(self, high_card_rank):
        super().__init__(HandStrength.STRAIGHT_FLUSH)
        if high_card_rank is None:
            raise ValueError("high_card_rank must be set")
        self.high_card_rank = high_card_rank

    def compare_same_rank(self, other):
        return self.high_card_rank.compare_to(other.high_card_rank)

    def describe_hand(self):
        return "Straight flush, {} high".format(self.high_card_rank)


class RoyalFlush(HandRank):
    def __init__(self, suit):
        super().__init__(HandStrength.ROYAL_FLUSH)
        if suit is None:
            raise ValueError("suit must be set")
        self.suit = suit

    def compare_same_rank(self, other):
        return 0

    def describe_hand(self):
        return "Royal flush of {}".format(self.suit)


class NotRankableHandRank(HandRank):
    def __init__(self, cards):
        super().__init__(None)
        self.cards = cards

    def compare_to(self, other):
        return 0

    def compare_same_rank(self, other):
        return 0

    def describe_hand(self):
        return "An unrankable hand with {} card(s)".format(len(self.cards))

    def compare_same_rank(self, other):
        return 0
