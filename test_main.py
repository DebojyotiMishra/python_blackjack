import unittest
from main import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_shuffle_deck(self):
        # Test if the deck is shuffled
        original_deck = self.deck.deck.copy()
        self.deck.shuffle_deck(self.deck.deck)
        shuffled_deck = self.deck.deck
        self.assertNotEqual(original_deck, shuffled_deck)

    def test_deal_card(self):
        # Test if the correct number of cards are dealt
        num_cards = 3
        dealt_cards = self.deck.deal_card(num_cards)
        self.assertEqual(len(dealt_cards), num_cards)

        # Test if the dealt cards are removed from the deck
        remaining_cards = len(self.deck.deck)
        self.assertEqual(remaining_cards, 52 - num_cards)

    def test_deck_initialization(self):
        # Test if the deck is initialized correctly
        expected_deck = [('A', 'Hearts'), ('2', 'Hearts'), ('3', 'Hearts'), ('4', 'Hearts'), ('5', 'Hearts'), ('6', 'Hearts'), ('7', 'Hearts'), ('8', 'Hearts'), ('9', 'Hearts'), ('10', 'Hearts'), ('J', 'Hearts'), ('Q', 'Hearts'), ('K', 'Hearts'), ('A', 'Diamonds'), ('2', 'Diamonds'), ('3', 'Diamonds'), ('4', 'Diamonds'), ('5', 'Diamonds'), ('6', 'Diamonds'), ('7', 'Diamonds'), ('8', 'Diamonds'), ('9', 'Diamonds'), ('10', 'Diamonds'), ('J', 'Diamonds'), ('Q', 'Diamonds'), ('K', 'Diamonds'), ('A', 'Clubs'), ('2', 'Clubs'), ('3', 'Clubs'), ('4', 'Clubs'), ('5', 'Clubs'), ('6', 'Clubs'), ('7', 'Clubs'), ('8', 'Clubs'), ('9', 'Clubs'), ('10', 'Clubs'), ('J', 'Clubs'), ('Q', 'Clubs'), ('K', 'Clubs'), ('A', 'Spades'), ('2', 'Spades'), ('3', 'Spades'), ('4', 'Spades'), ('5', 'Spades'), ('6', 'Spades'), ('7', 'Spades'), ('8', 'Spades'), ('9', 'Spades'), ('10', 'Spades'), ('J', 'Spades'), ('Q', 'Spades'), ('K', 'Spades')]
        self.assertEqual(self.deck.deck, expected_deck)

if __name__ == '__main__':
    unittest.main()