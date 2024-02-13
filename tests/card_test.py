import unittest

from pokerhands.card import Card
from pokerhands.rank import Rank
from pokerhands.suit import Suit


class CardTest(unittest.TestCase):
    def test_card_suit_null(self):
        self.assertRaises(ValueError, lambda: Card(Rank.TWO, None))

    def test_card_rank_null(self):
        self.assertRaises(ValueError, lambda: Card(None, Suit.CLUBS))

    def test_card_two_of_clubs(self):
        card = Card(Rank.TWO, Suit.CLUBS)
        self.assertEqual("two of clubs", str(card))

    def test_card_ace_of_clubs(self):
        card = Card(Rank.ACE, Suit.CLUBS)
        self.assertEqual("ace of clubs", str(card))

    def test_king_of_hearts(self):
        card = Card(Rank.KING, Suit.HEARTS)
        self.assertEqual("king of hearts", str(card))

    def test_card_compare_to(self):
        king_hearts_1 = Card(Rank.KING, Suit.HEARTS)
        king_hearts_2 = Card(Rank.KING, Suit.HEARTS)
        self.assertEqual(0, king_hearts_1.compare_to(king_hearts_2))

        king_clubs = Card(Rank.KING, Suit.CLUBS)
        self.assertEqual(0, king_hearts_1.compare_to(king_clubs))

        queen_hearts = Card(Rank.QUEEN, Suit.HEARTS)
        self.assertEqual(1, king_hearts_1.compare_to(queen_hearts))

    def test_equals(self):
        king_hearts_1 = Card(Rank.KING, Suit.HEARTS)
        king_hearts_2 = Card(Rank.KING, Suit.HEARTS)
        self.assertEqual(king_hearts_1, king_hearts_2)

        king_clubs = Card(Rank.KING, Suit.CLUBS)
        self.assertNotEqual(king_hearts_1, king_clubs)

        queen_hearts = Card(Rank.QUEEN, Suit.HEARTS)
        self.assertNotEqual(king_hearts_1, queen_hearts)


if __name__ == '__main__':
    unittest.main()
