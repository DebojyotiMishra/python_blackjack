import random

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = {'A': 1,
                    '2': 2,
                    '3': 3,
                    '4': 4,
                    '5': 5,
                    '6': 6,
                    '7': 7,
                    '8': 8,
                    '9': 9,
                    '10': 10,
                    'J': 10,
                    'Q': 10,
                    'K': 10}

        self.deck = [(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle_deck(self):
        """
        Shuffles the given deck of cards.

        Parameters:
        deck (list): The list representing the deck of cards.

        Returns:
        None
        """
        random.shuffle(self.deck)
        
    def deal_card(self, num_cards=1):
        """
        Deals a specified number of cards from the deck.
        
        Args:
            num_cards (int): The number of cards to deal. Defaults to 1.
        
        Returns:
            list: A list of cards dealt from the deck.
        """
        return [self.deck.pop() for _ in range(num_cards)]

deck = Deck()
deck.shuffle_deck()
print(deck.deal_card(5))
