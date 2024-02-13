import unittest

from pokerhands.card import Card
from pokerhands.handrank.ranks import *
from pokerhands.rank import Rank
from pokerhands.suit import Suit


class HandRankTest(unittest.TestCase):

    # TODO: Automate these comparisons
    def test_compare_to(self):
        royal_flush_clubs = RoyalFlush(Suit.CLUBS)
        royal_flush_spades = RoyalFlush(Suit.SPADES)
        self.assertEqual(0, royal_flush_clubs.compare_to(royal_flush_spades))

        straight_flush_jack = StraightFlush(Rank.JACK)
        self.assertTrue(royal_flush_clubs.compare_to(straight_flush_jack) > 0)

        straight_flush_ten = StraightFlush(Rank.TEN)
        self.assertTrue(straight_flush_jack.compare_to(straight_flush_ten) > 0)
        self.assertTrue(straight_flush_ten.compare_to(straight_flush_jack) < 0)

        straight_flush_ten_2 = StraightFlush(Rank.TEN)
        self.assertEqual(0, straight_flush_ten.compare_to(straight_flush_ten_2))

        four_of_a_kind_king = FourOfAKind(Rank.KING)
        self.assertTrue(royal_flush_clubs.compare_to(four_of_a_kind_king) > 0)
        self.assertTrue(straight_flush_ten.compare_to(four_of_a_kind_king) > 0)

        four_of_a_kind_queen = FourOfAKind(Rank.QUEEN)
        self.assertTrue(four_of_a_kind_queen.compare_to(four_of_a_kind_king) < 0)

        full_house_five_three = FullHouse(Rank.FIVE, Rank.THREE)
        self.assertTrue(royal_flush_clubs.compare_to(full_house_five_three) > 0)
        self.assertTrue(straight_flush_ten.compare_to(full_house_five_three) > 0)
        self.assertTrue(four_of_a_kind_queen.compare_to(full_house_five_three) > 0)

        full_house_three_two = FullHouse(Rank.THREE, Rank.TWO)
        self.assertTrue(full_house_five_three.compare_to(full_house_three_two) > 0)

        full_house_five_two = FullHouse(Rank.FIVE, Rank.TWO)
        self.assertTrue(full_house_five_three.compare_to(full_house_five_two) > 0)
        self.assertTrue(full_house_five_two.compare_to(full_house_three_two) > 0)

        flush_queen_three_cards = [
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.THREE, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        flush_queen_three = Flush(flush_queen_three_cards)
        self.assertTrue(royal_flush_clubs.compare_to(flush_queen_three) > 0)
        self.assertTrue(straight_flush_ten.compare_to(flush_queen_three) > 0)
        self.assertTrue(four_of_a_kind_queen.compare_to(flush_queen_three) > 0)
        self.assertTrue(full_house_five_three.compare_to(flush_queen_three) > 0)

        flush_queen_three_2 = Flush(flush_queen_three_cards)
        self.assertEqual(0, flush_queen_three.compare_to(flush_queen_three_2))

        flush_queen_two = Flush([
            Card(Rank.NINE, Suit.HEARTS),
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.HEARTS),
            Card(Rank.JACK, Suit.HEARTS),
            Card(Rank.TEN, Suit.HEARTS),
        ])
        self.assertTrue(flush_queen_three.compare_to(flush_queen_two) > 0)

        flush_king_two = Flush([
            Card(Rank.NINE, Suit.CLUBS),
            Card(Rank.TWO, Suit.CLUBS),
            Card(Rank.KING, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ])
        self.assertTrue(flush_king_two.compare_to(flush_queen_three) > 0)
        self.assertTrue(flush_king_two.compare_to(flush_queen_two) > 0)

        straight_king = Straight(Rank.KING)
        self.assertTrue(royal_flush_clubs.compare_to(straight_king) > 0)
        self.assertTrue(straight_flush_ten.compare_to(straight_king) > 0)
        self.assertTrue(four_of_a_kind_queen.compare_to(straight_king) > 0)
        self.assertTrue(full_house_five_three.compare_to(straight_king) > 0)
        self.assertTrue(flush_queen_three.compare_to(straight_king) > 0)

        straight_nine = Straight(Rank.NINE)
        self.assertTrue(straight_king.compare_to(straight_nine) > 0)

        three_of_a_kind_six = ThreeOfAKind(Rank.SIX)
        self.assertTrue(royal_flush_clubs.compare_to(three_of_a_kind_six) > 0)
        self.assertTrue(straight_flush_ten.compare_to(three_of_a_kind_six) > 0)
        self.assertTrue(four_of_a_kind_queen.compare_to(three_of_a_kind_six) > 0)
        self.assertTrue(full_house_five_three.compare_to(three_of_a_kind_six) > 0)
        self.assertTrue(flush_queen_three.compare_to(three_of_a_kind_six) > 0)
        self.assertTrue(straight_king.compare_to(three_of_a_kind_six) > 0)

        two_pair_ten_five_three = TwoPair(Rank.TEN, Rank.FIVE, Rank.THREE)
        self.assertTrue(royal_flush_clubs.compare_to(two_pair_ten_five_three) > 0)
        self.assertTrue(straight_flush_ten.compare_to(two_pair_ten_five_three) > 0)
        self.assertTrue(four_of_a_kind_queen.compare_to(two_pair_ten_five_three) > 0)
        self.assertTrue(full_house_five_three.compare_to(two_pair_ten_five_three) > 0)
        self.assertTrue(flush_queen_three.compare_to(two_pair_ten_five_three) > 0)
        self.assertTrue(straight_king.compare_to(two_pair_ten_five_three) > 0)
        two_pair_ten_five_three_2 = TwoPair(Rank.TEN, Rank.FIVE, Rank.THREE)
        self.assertEqual(0, two_pair_ten_five_three_2.compare_to(two_pair_ten_five_three))

        two_pair_ten_five_two = TwoPair(Rank.TEN, Rank.FIVE, Rank.TWO)
        self.assertTrue(two_pair_ten_five_three.compare_to(two_pair_ten_five_two) > 0)

        two_pair_ten_four_two = TwoPair(Rank.TEN, Rank.FOUR, Rank.TWO)
        self.assertTrue(two_pair_ten_five_three.compare_to(two_pair_ten_four_two) > 0)

        two_pair_nine_five_two = TwoPair(Rank.NINE, Rank.FIVE, Rank.TWO)
        self.assertTrue(two_pair_ten_five_three.compare_to(two_pair_nine_five_two) > 0)

        one_pair_ten_765 = OnePair(Rank.TEN, [Rank.SEVEN, Rank.SIX, Rank.FIVE])
        self.assertTrue(royal_flush_clubs.compare_to(one_pair_ten_765) > 0)
        self.assertTrue(straight_flush_ten.compare_to(one_pair_ten_765) > 0)
        self.assertTrue(four_of_a_kind_queen.compare_to(one_pair_ten_765) > 0)
        self.assertTrue(full_house_five_three.compare_to(one_pair_ten_765) > 0)
        self.assertTrue(flush_queen_three.compare_to(one_pair_ten_765) > 0)
        self.assertTrue(straight_king.compare_to(one_pair_ten_765) > 0)
        self.assertTrue(two_pair_ten_five_three.compare_to(one_pair_ten_765) > 0)

        one_pair_ten_763 = OnePair(Rank.TEN, [Rank.SEVEN, Rank.SIX, Rank.THREE])
        self.assertTrue(one_pair_ten_765.compare_to(one_pair_ten_763) > 0)

        one_pair_ten_763_2 = OnePair(Rank.TEN, [Rank.SEVEN, Rank.SIX, Rank.THREE])
        self.assertEqual(0, one_pair_ten_763.compare_to(one_pair_ten_763_2))

        one_pair_ten_743 = OnePair(Rank.TEN, [Rank.SEVEN, Rank.FOUR, Rank.THREE])
        self.assertTrue(one_pair_ten_763.compare_to(one_pair_ten_743) > 0)

        one_pair_ten_943 = OnePair(Rank.NINE, [Rank.SEVEN, Rank.FOUR, Rank.THREE])
        self.assertTrue(one_pair_ten_763.compare_to(one_pair_ten_943) > 0)

        high_ace_queen_975 = HighCard([
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.SEVEN, Suit.CLUBS),
            Card(Rank.FIVE, Suit.CLUBS),
        ])
        self.assertTrue(royal_flush_clubs.compare_to(high_ace_queen_975) > 0)
        self.assertTrue(straight_flush_ten.compare_to(high_ace_queen_975) > 0)
        self.assertTrue(four_of_a_kind_queen.compare_to(high_ace_queen_975) > 0)
        self.assertTrue(full_house_five_three.compare_to(high_ace_queen_975) > 0)
        self.assertTrue(flush_queen_three.compare_to(high_ace_queen_975) > 0)
        self.assertTrue(straight_king.compare_to(high_ace_queen_975) > 0)
        self.assertTrue(two_pair_ten_five_three.compare_to(high_ace_queen_975) > 0)
        self.assertTrue(one_pair_ten_765.compare_to(high_ace_queen_975) > 0)

        high_ace_queen_975_2 = HighCard([
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.SEVEN, Suit.CLUBS),
            Card(Rank.FIVE, Suit.CLUBS),
        ])
        self.assertEqual(0, high_ace_queen_975.compare_to(high_ace_queen_975_2))

        high_ace_queen_875 = HighCard([
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.EIGHT, Suit.DIAMONDS),
            Card(Rank.SEVEN, Suit.CLUBS),
            Card(Rank.FIVE, Suit.CLUBS),
        ])
        self.assertTrue(high_ace_queen_975.compare_to(high_ace_queen_875) > 0)

        not_rankable_0 = NotRankableHandRank(None)
        not_rankable_1 = NotRankableHandRank([])
        self.assertEqual(0, not_rankable_0.compare_to(not_rankable_1))
        self.assertEqual(0, not_rankable_0.compare_same_rank(not_rankable_1))

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
