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
        self.assertEqual(0, hand_six.compare_to(hand_two))

        cards = [
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.KING, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.TEN, Suit.CLUBS),
        ]
        royal_flush = Hand(cards)
        self.assertEqual(9, royal_flush.compare_to(hand_two))
        self.assertEqual(-1, hand_two.compare_to(royal_flush))

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

    def test_get_best_hand_from_deck(self):
        cards = Deck().pick(7)
        originalHand = Hand(cards)
        bestHand = originalHand.get_best_hand()
        #self.assertEqual(9, bestHand.get_rank().get_hand_strength().value)

    def test_get_best_hand_royal_flush(self):

        cards = [
            # Straight hand
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.THREE, Suit.DIAMONDS),
            Card(Rank.FIVE, Suit.CLUBS),
            Card(Rank.SEVEN, Suit.SPADES),
            Card(Rank.EIGHT, Suit.HEARTS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.SPADES),
            Card(Rank.QUEEN, Suit.HEARTS),
            Card(Rank.KING, Suit.DIAMONDS),
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.TWO, Suit.SPADES),

            # Royal Flush
            Card(Rank.TEN, Suit.HEARTS),
            Card(Rank.JACK, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.HEARTS),
            Card(Rank.KING, Suit.HEARTS),
            Card(Rank.ACE, Suit.HEARTS)
        ]

        besthand = Hand(cards).get_best_hand()

        expected_best_hand_cards = [
            Card(Rank.TEN, Suit.HEARTS),
            Card(Rank.JACK, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.HEARTS),
            Card(Rank.KING, Suit.HEARTS),
            Card(Rank.ACE, Suit.HEARTS)
        ]

        self.assertTrue(self.compare_card_arrays(expected_best_hand_cards, besthand.get_cards()))
        self.assertEqual(Hand(expected_best_hand_cards).describe_hand_rank(), besthand.describe_hand_rank())

    def test_get_best_hand_straight_flush(self):

        cards = [
            # Straight Flush (higher)
            Card(Rank.TEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.KING, Suit.CLUBS),
            Card(Rank.ACE, Suit.CLUBS),
            
            # Straight Flush (lower)
            Card(Rank.FIVE, Suit.CLUBS),
            Card(Rank.SIX, Suit.CLUBS),
            Card(Rank.SEVEN, Suit.CLUBS),
            Card(Rank.EIGHT, Suit.CLUBS),
            Card(Rank.NINE, Suit.CLUBS),

            # Four of a Kind
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.TWO, Suit.CLUBS),
            Card(Rank.TWO, Suit.SPADES),
            Card(Rank.SEVEN, Suit.SPADES),
        ]

        besthand = Hand(cards).get_best_hand()

        expected_best_hand_cards = [
            Card(Rank.TEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.CLUBS),
            Card(Rank.QUEEN, Suit.CLUBS),
            Card(Rank.KING, Suit.CLUBS),
            Card(Rank.ACE, Suit.CLUBS),
        ]

        self.assertTrue(self.compare_card_arrays(expected_best_hand_cards, besthand.get_cards()))
        self.assertEqual(Hand(expected_best_hand_cards).describe_hand_rank(), besthand.describe_hand_rank())

    def test_get_best_hand_four_of_a_kind(self):

        cards = [
            # Four of a Kind (higher)
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.TWO, Suit.CLUBS),
            Card(Rank.TWO, Suit.SPADES),
            Card(Rank.THREE, Suit.SPADES),
            
            # Four of a Kind (lower)
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.TWO, Suit.CLUBS),
            Card(Rank.TWO, Suit.SPADES),
            Card(Rank.FOUR, Suit.HEARTS),
        ]

        besthand = Hand(cards).get_best_hand()

        expected_best_hand_cards = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.TWO, Suit.CLUBS),
            Card(Rank.TWO, Suit.SPADES),
            Card(Rank.FOUR, Suit.HEARTS),
        ]

        self.assertTrue(self.compare_card_arrays(expected_best_hand_cards, besthand.get_cards()))
        self.assertEqual(Hand(expected_best_hand_cards).describe_hand_rank(), besthand.describe_hand_rank())


    def test_get_best_hand_full_house(self):

        cards = [
            Card(Rank.THREE, Suit.HEARTS),
            Card(Rank.THREE, Suit.DIAMONDS),
            Card(Rank.THREE, Suit.SPADES),
            Card(Rank.FOUR, Suit.SPADES),
            Card(Rank.FOUR, Suit.CLUBS),            
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.SIX, Suit.HEARTS),
            Card(Rank.SIX, Suit.DIAMONDS),
            Card(Rank.SIX, Suit.SPADES),
        ]

        expected_best_hand_cards = [
            Card(Rank.FOUR, Suit.SPADES),
            Card(Rank.FOUR, Suit.CLUBS),
            Card(Rank.SIX, Suit.HEARTS),
            Card(Rank.SIX, Suit.DIAMONDS),
            Card(Rank.SIX, Suit.SPADES),
        ]

        besthand = Hand(cards).get_best_hand()

        self.assertTrue(self.compare_card_arrays(expected_best_hand_cards, besthand.get_cards()))
        self.assertEqual(Hand(expected_best_hand_cards).describe_hand_rank(), besthand.describe_hand_rank())

    def test_get_best_hand_flush(self):

        lower_flush_cards = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.FOUR, Suit.HEARTS),
            Card(Rank.SIX, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.HEARTS),
            Card(Rank.TEN, Suit.HEARTS),
        ]

        higher_flush_cards = [
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.FOUR, Suit.DIAMONDS),
            Card(Rank.SIX, Suit.DIAMONDS),
            Card(Rank.EIGHT, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.DIAMONDS),
        ]

        cards = lower_flush_cards + higher_flush_cards

        low_flush_hand = Hand(lower_flush_cards)
        high_flush_hand = Hand(higher_flush_cards)

        self.assertEqual(-1, low_flush_hand.compare_to(high_flush_hand))

        besthand = Hand(cards).get_best_hand()

        self.assertTrue(self.compare_card_arrays(higher_flush_cards, besthand.get_cards()))
        self.assertEqual(Hand(higher_flush_cards).describe_hand_rank(), besthand.describe_hand_rank())


    def test_get_best_hand_straight(self):

        cards = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.THREE, Suit.DIAMONDS),
            Card(Rank.FIVE, Suit.CLUBS),
            Card(Rank.SEVEN, Suit.SPADES),
            Card(Rank.EIGHT, Suit.HEARTS),
            Card(Rank.NINE, Suit.DIAMONDS),
            Card(Rank.TEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.SPADES),
            Card(Rank.QUEEN, Suit.HEARTS),
            Card(Rank.KING, Suit.DIAMONDS),
            Card(Rank.ACE, Suit.CLUBS),
            Card(Rank.TWO, Suit.SPADES)
        ]

        besthand = Hand(cards).get_best_hand()

        expected_best_hand_cards = [
            Card(Rank.TEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.SPADES),
            Card(Rank.QUEEN, Suit.HEARTS),
            Card(Rank.KING, Suit.DIAMONDS),
            Card(Rank.ACE, Suit.CLUBS),
        ]

        self.assertTrue(self.compare_card_arrays(expected_best_hand_cards, besthand.get_cards()))
        self.assertEqual(Hand(expected_best_hand_cards).describe_hand_rank(), besthand.describe_hand_rank())

    def test_get_best_hand_three_of_a_kind(self):

        cards = [
            Card(Rank.TWO, Suit.CLUBS),
            Card(Rank.FOUR, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.DIAMONDS),
            Card(Rank.SEVEN, Suit.CLUBS),
            Card(Rank.TEN, Suit.HEARTS),
            Card(Rank.JACK, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.SPADES),
        ]

        besthand = Hand(cards).get_best_hand()

        expected_best_hand_cards = [
            Card(Rank.SEVEN, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.DIAMONDS),
            Card(Rank.SEVEN, Suit.CLUBS),
            Card(Rank.JACK, Suit.HEARTS),
            Card(Rank.QUEEN, Suit.SPADES),
        ]

        self.assertTrue(self.compare_card_arrays(expected_best_hand_cards, besthand.get_cards()))
        self.assertEqual(Hand(expected_best_hand_cards).describe_hand_rank(), besthand.describe_hand_rank())

    def test_find_best_hand_two_pair(self):

        cards = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.THREE, Suit.HEARTS),
            Card(Rank.SIX, Suit.CLUBS),
            Card(Rank.THREE, Suit.SPADES),
            Card(Rank.FOUR, Suit.HEARTS),
            Card(Rank.SIX, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.DIAMONDS),
        ]

        expected_best_hand_cards = [
            Card(Rank.THREE, Suit.HEARTS),
            Card(Rank.THREE, Suit.SPADES),
            Card(Rank.SIX, Suit.CLUBS),
            Card(Rank.SIX, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.DIAMONDS),
        ]

        besthand = Hand(cards).get_best_hand()

        self.assertTrue(self.compare_card_arrays(expected_best_hand_cards, besthand.get_cards()))
        self.assertEqual(Hand(expected_best_hand_cards).describe_hand_rank(), besthand.describe_hand_rank())

    def test_find_best_hand_one_pair(self):

        cards = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.THREE, Suit.HEARTS),
            Card(Rank.SIX, Suit.CLUBS),
            Card(Rank.FIVE, Suit.SPADES),
            Card(Rank.EIGHT, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.DIAMONDS),
        ]

        expected_best_hand_cards = [
            Card(Rank.TWO, Suit.HEARTS),
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.SIX, Suit.CLUBS),
            Card(Rank.EIGHT, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.DIAMONDS),
        ]

        besthand = Hand(cards).get_best_hand()

        self.assertTrue(self.compare_card_arrays(expected_best_hand_cards, besthand.get_cards()))
        self.assertEqual(Hand(expected_best_hand_cards).describe_hand_rank(), besthand.describe_hand_rank())

    def test_find_best_hand_highcard(self):

        cards = [
            Card(Rank.TWO, Suit.DIAMONDS),
            Card(Rank.THREE, Suit.HEARTS),
            Card(Rank.SIX, Suit.CLUBS),
            Card(Rank.FIVE, Suit.SPADES),
            Card(Rank.EIGHT, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.DIAMONDS),
        ]

        expected_best_hand_cards = [
            Card(Rank.THREE, Suit.HEARTS),
            Card(Rank.SIX, Suit.CLUBS),
            Card(Rank.FIVE, Suit.SPADES),
            Card(Rank.EIGHT, Suit.HEARTS),
            Card(Rank.SEVEN, Suit.DIAMONDS),
        ]

        besthand = Hand(cards).get_best_hand()

        self.assertTrue(self.compare_card_arrays(expected_best_hand_cards, besthand.get_cards()))
        self.assertEqual(Hand(expected_best_hand_cards).describe_hand_rank(), besthand.describe_hand_rank())


    def compare_card_arrays(self, cards1, cards2):
        # Sort the cards in both arrays based on rank and suit
        sorted_cards1 = sorted(cards1, key=lambda card: (card.rank.value, card.suit.value))
        sorted_cards2 = sorted(cards2, key=lambda card: (card.rank.value, card.suit.value))

        # Compare the sorted arrays element-wise
        for card1, card2 in zip(sorted_cards1, sorted_cards2):
            if card1.rank != card2.rank or card1.suit != card2.suit:
                return False  # Arrays are not equal
        return True  # Arrays are equal   
        
if __name__ == '__main__':
    unittest.main()
