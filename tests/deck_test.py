import unittest
from pokerhands.deck import Deck, NotEnoughCardsException


class DeckTest(unittest.TestCase):
    def test_deck_size(self):
        deck = Deck()
        self.assertEqual(52, deck.number_of_cards(), "A deck must start with 52 cards")

    def test_deck_pick_hand(self):
        deck = Deck()
        cards = deck.pick(5)
        self.assertEqual(5, len(cards))
        self.assertEqual(47, deck.number_of_cards())

    def test_deck_pick_zero(self):
        deck = Deck()
        cards = deck.pick(0)
        self.assertEqual(0, len(cards))
        self.assertEqual(52, deck.number_of_cards())

    def test_deck_pick_52(self):
        deck = Deck()
        cards = deck.pick(52)
        self.assertEqual(52, len(cards))
        self.assertEqual(0, deck.number_of_cards())


if __name__ == '__main__':
    unittest.main()
