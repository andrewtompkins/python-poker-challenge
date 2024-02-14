from copy import deepcopy
from itertools import groupby
from .handrank.ranks import RoyalFlush, StraightFlush, FullHouse, HighCard, FourOfAKind, ThreeOfAKind, TwoPair, OnePair, Flush, Straight, NotRankableHandRank
from .rank import Rank
from itertools import combinations
from collections import OrderedDict


class Hand:

    def __init__(self, cards):
        self._cards = deepcopy(cards) if cards is not None else []
        self._rank = None

    def number_of_cards(self):
        return len(self._cards)

    def get_cards(self):
        return self._cards

    def describe_hand_rank(self):           
        return self.get_rank().describe_hand();

    def compare_to(self, other):
        return self.get_rank().compare_to(other.get_rank());

    def get_rank(self):
        if self._rank is None:
            if len(self._cards) != 5:
                self._rank = NotRankableHandRank(self._cards)
                return self._rank

            rank, cards = self.get_rank_for_cards(self._cards)
            self._rank = rank
        return self._rank

    def get_best_hand(self):
        rank, cards = self.get_rank_for_cards(self._cards)
        return Hand(cards)
        
    def get_rank_for_cards(self, cards_to_evaluate):

        if len(cards_to_evaluate) < 5:
            return NotRankableHandRank(cards_to_evaluate), cards_to_evaluate

        # Royal or Straight Flush
        straight_flush = Hand.find_best_straight_flush(cards_to_evaluate)
        if straight_flush is not None:

            highestRank = max(straight_flush, key=lambda card: card.rank)

            if highestRank.rank.value == 14:
                return RoyalFlush(highestRank.suit), straight_flush
            else:
                return StraightFlush(highestRank.rank), straight_flush

        # Four Of A Kind
        four_of_a_kind_rank, four_of_a_kind_cards = Hand.get_cards_and_rank_for_x_of_a_kind(cards_to_evaluate, 4)
        if four_of_a_kind_rank is not None:
            return FourOfAKind(four_of_a_kind_rank), four_of_a_kind_cards

        # Full House
        three_of_a_kind_rank, pair_rank, full_house_cards = Hand.find_full_house(cards_to_evaluate)
        if three_of_a_kind_rank is not None:
            return FullHouse(three_of_a_kind_rank, pair_rank), full_house_cards

        # Flush
        flush = Hand.get_highest_ranked_flush(cards_to_evaluate)
        if flush is not None:
            return Flush(flush), flush

        # Straight
        straight = Hand.find_best_straight(cards_to_evaluate)
        if straight is not None:
            highestRank = max(straight, key=lambda card: card.rank)
            return Straight(highestRank.rank), straight

        # Three Of A Kind
        three_of_a_kind_rank, three_of_a_kind_cards = Hand.get_cards_and_rank_for_x_of_a_kind(cards_to_evaluate, 3)
        if three_of_a_kind_rank is not None:
            return ThreeOfAKind(three_of_a_kind_rank), three_of_a_kind_cards              
    
        # Two Pairs
        twopair_pairs, twopair_singles, twopair_cards = Hand.get_highest_x_pair_hand(cards_to_evaluate, 2)
        if len(twopair_pairs) == 2:
            return TwoPair(twopair_pairs[0], twopair_pairs[1], twopair_singles[0]), twopair_cards

        # One Pair
        onepair_pairs, onepair_singles, onepair_cards = Hand.get_highest_x_pair_hand(cards_to_evaluate, 1)
        if len(onepair_pairs) == 1:
            return OnePair(onepair_pairs[0], onepair_singles), onepair_cards

        # High Card
        cards_to_evaluate.sort(reverse=True)
        highest_five_cards = cards_to_evaluate[:min(5, len(cards_to_evaluate))]
        return HighCard(highest_five_cards), highest_five_cards

    def find_best_straight_flush(cards):
        straight_flushes = []

        for suit in set(card.suit for card in cards):
            flush_cards = [card for card in cards if card.suit == suit]

            straight_flush = Hand.find_best_straight(flush_cards)

            if straight_flush and len(straight_flush) >= 5:
                straight_flushes.append(straight_flush)

        # Filter out straight flushes with more than 5 cards
        straight_flushes = [sf for sf in straight_flushes if len(sf) == 5]

        if straight_flushes:
            return max(straight_flushes, key=lambda straight_flush: max(card.rank.value for card in straight_flush))

        return None
            
    def find_best_straight(cards):
        # Remove duplicates while preserving order
        unique_cards = []
        seen_ranks = set()
        for card in cards:
            if card.rank not in seen_ranks:
                unique_cards.append(card)
                seen_ranks.add(card.rank)

        # Sort the unique cards by rank value
        unique_cards.sort(key=lambda card: card.rank.value, reverse=True)

        # Initialize variables to track the current and maximum straight lengths
        straight_length = 1
        max_straight_length = 1
        best_straight = []

        # Iterate through the sorted cards starting from the second card
        for i in range(1, len(unique_cards)):
            # Check if the current card's rank is one less than the previous card's rank
            if unique_cards[i].rank.value == unique_cards[i - 1].rank.value - 1:
                straight_length += 1
                # Update the maximum straight length and best straight if needed
                if straight_length >= max_straight_length:
                    max_straight_length = straight_length
                    best_straight = unique_cards[i - max_straight_length + 1:i + 1]
                    # Trim the result if it exceeds 5 cards
                    if len(best_straight) > 5:
                        best_straight = best_straight[:5]
            else:
                # Reset the straight length
                straight_length = 1

        # Return the best straight found if it contains at least 5 cards
        if max_straight_length >= 5:
            return best_straight

        # Otherwise, return None
        return None

    def get_highest_ranked_flush(cards):
        suits = set(card.suit for card in cards)  # Extract unique suits from the cards
        highest_flush = []

        # Iterate over each suit
        for suit in suits:
            flush_cards = [card for card in cards if card.suit == suit]
            if len(flush_cards) >= 5:  # Check if there are at least 5 cards of the same suit
                flush_cards.sort(reverse=True)  # Sort the flush cards in descending order
                highest_flush = flush_cards[:5]  # Take only the top 5 cards
                break  # Exit the loop once a flush is found

        if not highest_flush:
            return None

        # Find the highest flush based on comparing cards from highest to lowest rank
        for suit in suits:
            flush_cards = [card for card in cards if card.suit == suit]
            if len(flush_cards) >= 5:
                flush_cards.sort(reverse=True)
                for i in range(5):
                    if flush_cards[i].rank != highest_flush[i].rank:
                        if flush_cards[i].rank.value > highest_flush[i].rank.value:
                            highest_flush = flush_cards[:5]
                        break

        return highest_flush

    def get_cards_and_rank_for_x_of_a_kind(cards, x):
        rank_counts = {}  # Dictionary to store the count of each rank
        for card in cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        # Sort rank counts in descending order by count, then by rank itself
        sorted_rank_counts = sorted(rank_counts.items(), key=lambda item: (-item[1], -item[0].value))

        # Find the x-of-a-kind rank
        x_of_a_kind_rank = None
        for rank, count in sorted_rank_counts:
            if count >= x:
                x_of_a_kind_rank = rank
                break

        # If no x-of-a-kind rank is found, return None, []
        if x_of_a_kind_rank is None:
            return None, []

        # Find all cards of the x-of-a-kind rank
        x_of_a_kind_cards = [card for card in cards if card.rank == x_of_a_kind_rank]

        # Sort x_of_a_kind_cards by rank in descending order
        x_of_a_kind_cards.sort(reverse=True)

        # Take the first x cards to form the x-of-a-kind hand
        x_of_a_kind_hand = x_of_a_kind_cards[:x]

        # Find all cards not in the x-of-a-kind hand
        other_cards = [card for card in cards if card.rank != x_of_a_kind_rank]

        # Sort other cards by rank in descending order
        other_cards.sort(reverse=True)

        # Take as many highest ranking cards as needed to complete the hand
        num_missing_cards = 5 - len(x_of_a_kind_hand)
        other_cards = other_cards[:num_missing_cards]

        # Combine the x-of-a-kind hand and the other cards to form the result
        result = x_of_a_kind_hand + other_cards

        return x_of_a_kind_rank, result

    def find_full_house(cards):
        # Create a dictionary to store the count of each rank
        rank_counts = {}
        for card in cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1

        full_houses = []

        # Iterate over all possible combinations of three-of-a-kind and pair
        for three_rank, three_count in rank_counts.items():
            if three_count < 3:
                continue  # Skip ranks with less than three cards

            # Remove the cards used in the three-of-a-kind from the pool of cards
            remaining_cards = [card for card in cards if card.rank != three_rank]

            # Find all pairs that don't overlap with the triple
            pairs = [pair_rank for pair_rank, pair_count in rank_counts.items() if pair_count >= 2 and pair_rank != three_rank]

            # If there are no valid pairs, continue to the next triple
            if not pairs:
                continue

            # Select the highest-ranking pair
            max_pair_rank = max(pairs)

            # Found a valid pair
            triple_cards = [card for card in cards if card.rank == three_rank][:3]
            pair_cards = [card for card in remaining_cards if card.rank == max_pair_rank][:2]

            # Ensure both triple and pair are found
            if len(triple_cards) == 3 and len(pair_cards) == 2:
                full_houses.append((three_rank, max_pair_rank, triple_cards + pair_cards))

        # If there are full houses, return the one with the highest-ranking three-of-a-kind
        if full_houses:
            return max(full_houses, key=lambda hand: hand[0])
        else:
            return None, None, []

    def get_highest_x_pair_hand(cards, x):
        # Dictionary to store the count of each rank
        rank_counts = {rank: sum(card.rank == rank for card in cards) for rank in set(card.rank for card in cards)}

        # Filter pairs and singles
        pairs = [rank for rank, count in rank_counts.items() if count >= 2]
        singles = [rank for rank, count in rank_counts.items() if count == 1]

        # Sort pairs and singles
        pairs.sort(reverse=True)
        singles.sort(reverse=True)

        # Select x pairs for the hand
        selected_pairs = pairs[:x]

        # Select remaining singles based on highest rank
        remaining_singles = [rank for rank in singles if rank not in selected_pairs]
        selected_singles = sorted(remaining_singles, reverse=True)[:max(0, 5 - x * 2)]  # Ensure we have at most 5 cards in total

        # Collect the cards in the hand
        hand_cards = [card for card in cards if card.rank in selected_pairs or card.rank in selected_singles]

        return selected_pairs, selected_singles, hand_cards