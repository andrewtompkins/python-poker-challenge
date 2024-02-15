import unittest

from pokerhands.card import Card
from pokerhands.handrank.ranks import *
from pokerhands.rank import Rank
from pokerhands.suit import Suit


class HandRankTest(unittest.TestCase):

    # TODO: Automate these comparisons
    def test_compare_to(self):
        hands = [
            RoyalFlush(Suit.CLUBS),
            RoyalFlush(Suit.SPADES),

            StraightFlush(Rank.QUEEN),
            StraightFlush(Rank.JACK),

            FourOfAKind(Rank.KING),
            FourOfAKind(Rank.QUEEN),

            FullHouse(Rank.FIVE, Rank.THREE),
            FullHouse(Rank.FIVE, Rank.TWO),

            Flush([
                Card(Rank.NINE, Suit.CLUBS),
                Card(Rank.THREE, Suit.CLUBS),
                Card(Rank.QUEEN, Suit.CLUBS),
                Card(Rank.JACK, Suit.CLUBS),
                Card(Rank.TEN, Suit.CLUBS),
            ]),
            Flush([
                Card(Rank.NINE, Suit.HEARTS),
                Card(Rank.TWO, Suit.HEARTS),
                Card(Rank.QUEEN, Suit.HEARTS),
                Card(Rank.JACK, Suit.HEARTS),
                Card(Rank.TEN, Suit.HEARTS),
            ]),
            Straight(Rank.KING),
            Straight(Rank.NINE),

            ThreeOfAKind(Rank.SIX),
            ThreeOfAKind(Rank.FIVE),

            TwoPair(Rank.TEN, Rank.FIVE, Rank.THREE),
            TwoPair(Rank.TEN, Rank.FIVE, Rank.TWO),
            TwoPair(Rank.NINE, Rank.FIVE, Rank.TWO),

            NotRankableHandRank(None),
            NotRankableHandRank([]),
        ]

        # iterate through the array, and then for each hand in the array, iterate through all of the hands below it and compare
        for i, hand in enumerate(hands):
            for j, other_hand in enumerate(hands[i + 1:], start=i + 1):
                #print(f"Comparing {hand.describe_hand()} with {other_hand.describe_hand()}")
                if (hand.get_hand_strength() is None and other_hand.get_hand_strength() is None) or (hand.get_hand_strength() == HandStrength.ROYAL_FLUSH and other_hand.get_hand_strength() == HandStrength.ROYAL_FLUSH):
                    self.assertEqual(0, hand.compare_to(other_hand))
                    self.assertEqual(0, other_hand.compare_to(hand))
                else:
                    self.assertTrue(hand.compare_to(other_hand) > 0)
                    self.assertTrue(other_hand.compare_to(hand) < 0)


    def test_straight_flush(self):
        self.assertRaises(ValueError, lambda: StraightFlush(None))

    def test_four_of_a_kind(self):
        self.assertRaises(ValueError, lambda: FourOfAKind(None))

    def test_full_house(self):
        self.assertRaises(ValueError, lambda: FullHouse(None, None))
        self.assertRaises(ValueError, lambda: FullHouse(None, Rank.NINE))
        self.assertRaises(ValueError, lambda: FullHouse(Rank.EIGHT, None))

    def test_flush(self):
        self.assertRaises(ValueError, lambda: Flush(None))
        self.assertRaises(ValueError, lambda: Flush([]))
        self.assertRaises(ValueError, lambda: Flush([
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.THREE, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.DIAMONDS),
            Card(Rank.JACK, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.CLUBS),
            Card(Rank.TWO, Suit.CLUBS),
        ]))

    def test_straight(self):
        self.assertRaises(ValueError, lambda: Straight(None))

    def test_three_of_a_kind(self):
        self.assertRaises(ValueError, lambda: ThreeOfAKind(None))

    def test_two_pair(self):
        self.assertRaises(ValueError, lambda: TwoPair(None, Rank.FOUR, Rank.TWO))
        self.assertRaises(ValueError, lambda: TwoPair(Rank.FOUR, None, Rank.TWO))
        self.assertRaises(ValueError, lambda: TwoPair(Rank.FOUR, Rank.THREE, None))

    def test_one_pair(self):
        self.assertRaises(ValueError, lambda: OnePair(None, None))
        self.assertRaises(ValueError, lambda: OnePair(Rank.NINE, None))
        self.assertRaises(ValueError, lambda: OnePair(None, []))
        self.assertRaises(ValueError, lambda: OnePair(Rank.NINE, []))
        self.assertRaises(ValueError, lambda: OnePair(Rank.NINE, [
            Rank.ACE,
            Rank.QUEEN,
            Rank.EIGHT,
            Rank.SEVEN,
        ]))

    def test_high_card(self):
        self.assertRaises(ValueError, lambda: HighCard(None))
        self.assertRaises(ValueError, lambda: HighCard([]))
        self.assertRaises(ValueError, lambda: HighCard([
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.EIGHT, Suit.DIAMONDS),
            Card(Rank.SEVEN, Suit.CLUBS),
            Card(Rank.FIVE, Suit.CLUBS),
            Card(Rank.TWO, Suit.CLUBS),
        ]))


if __name__ == '__main__':
    unittest.main()
