import unittest
from pokerhands.hand import Hand
from pokerhands.card import Card
from pokerhands.rank import Rank
from pokerhands.suit import Suit
from pokerhands.deck import Deck


class HandTest(unittest.TestCase):

    def test_get_number_of_cards(self):
        deck = Deck()
        hand = Hand(deck.pick(5))
        self.assertEqual(5, hand.number_of_cards())

    def test_empty_hand(self):
        hand = Hand(None)
        self.assertEqual(0, hand.number_of_cards())

    def test_invalid_hand_rank(self):
        cards = [
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.KING, Suit.CLUBS),
        ]
        hand_two = Hand(cards)
        self.assertEqual("An unrankable hand with 2 card(s)", hand_two.describe_hand_rank())

        cards.append(Card(Rank.TWO, Suit.CLUBS))
        cards.append(Card(Rank.QUEEN, Suit.CLUBS))
        cards.append(Card(Rank.JACK, Suit.CLUBS))
        cards.append(Card(Rank.TEN, Suit.CLUBS))

        hand_six = Hand(cards)
        self.assertEqual("An unrankable hand with 6 card(s)", hand_six.describe_hand_rank())
        self.assertEqual(0, hand_two.compare_to(hand_six))

    def test_royal_flush(self):
        cards = [
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.KING, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        hand = Hand(cards)
        self.assertEqual("Royal flush of clubs", hand.describe_hand_rank())

    def test_four_of_a_kind(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.NINE, Suit.SPADES),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        hand = Hand(cards)
        self.assertEqual("Four of a kind of nines", hand.describe_hand_rank())

    def test_full_house(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.SPADES),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        hand = Hand(cards)
        self.assertEqual("Full house, nines over tens", hand.describe_hand_rank())

    def test_flush(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.THREE, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        hand = Hand(cards)
        self.assertEqual("Flush, queen high", hand.describe_hand_rank())

    def test_straight(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.KING, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        hand = Hand(cards)
        self.assertEqual("Straight, king high", hand.describe_hand_rank())

    def test_straight_flush(self):
        cards = [
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.KING, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.HEARTS),
            Card(Rank.JACK, Suit.HEARTS),
            Card(Rank.TEN, Suit.HEARTS),
        ]
        hand = Hand(cards)
        self.assertEqual("Straight flush, king high", hand.describe_hand_rank())

    def test_three_of_a_kind(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.SPADES),
            Card(Rank.TWO, Suit.CLUBS),
        ]
        hand = Hand(cards)
        self.assertEqual("Three of a kind of nines", hand.describe_hand_rank())

    def test_two_pairs(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.TEN, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.SPADES),
            Card(Rank.TWO, Suit.CLUBS),
        ]
        hand = Hand(cards)
        self.assertEqual("Two pair, tens and nines", hand.describe_hand_rank())

    def test_pair(self):
        cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.TEN, Suit.DIAMONDS),
            Card(Rank.SIX, Suit.SPADES),
            Card(Rank.TWO, Suit.CLUBS),
        ]
        hand = Hand(cards)
        self.assertEqual("One pair of nines", hand.describe_hand_rank())

    def test_high_card(self):
        cards = [
            Card(Rank.THREE, Suit.CLUBS),
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.TEN, Suit.DIAMONDS),
            Card(Rank.SIX, Suit.SPADES),
            Card(Rank.TWO, Suit.CLUBS),
        ]
        hand = Hand(cards)
        self.assertEqual("High card ten of diamonds", hand.describe_hand_rank())

    def test_flush_compared_to_straight(self):
        flush_cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.THREE, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        flush_hand = Hand(flush_cards)
        self.assertEqual("Flush, queen high", flush_hand.describe_hand_rank())

        straight_cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.KING, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        straight_hand = Hand(straight_cards)
        self.assertEqual("Straight, king high", straight_hand.describe_hand_rank())
        self.assertTrue(flush_hand.compare_to(straight_hand) > 0)

    def test_straight_compared_to_straight(self):
        low_straight_cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.EIGHT, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        low_straight_hand = Hand(low_straight_cards)
        self.assertEqual("Straight, queen high", low_straight_hand.describe_hand_rank())

        high_straight_cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.KING, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        high_straight_hand = Hand(high_straight_cards)
        self.assertEqual("Straight, king high", high_straight_hand.describe_hand_rank())
        self.assertTrue(low_straight_hand.compare_to(high_straight_hand) < 0)

if __name__ == '__main__':
    unittest.main()
