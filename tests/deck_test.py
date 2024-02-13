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

    def test_multiple_picks_balance(self):
        deck = Deck()

        # Ensure pick works when there are enough cards
        cards = deck.pick(5)
        self.assertEqual(len(cards), 5)
        cards = deck.pick(3)
        self.assertEqual(len(cards), 3)
        self.assertEqual(deck.number_of_cards(), deck.get_initial_deck_size() - 8)  # Ensure number of remaining cards is correct

    def test_pick_too_many_cards(self):
        deck = Deck()
        cards = deck.pick(52)
        with self.assertRaises(NotEnoughCardsException):
            deck.pick(3)  # Try to pick more cards than available

if __name__ == '__main__':
    unittest.main()
