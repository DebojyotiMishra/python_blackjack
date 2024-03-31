import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = {'A': 11,
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

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.dealer = dealer

    def add_cards(self, card_list):
        """
        Add one or more cards to the player's hand.

        Args:
            card_list (list): The list of cards to be added.

        Returns:
            None
        """
        self.cards.extend(card_list)
        self.calculate_value()

    def calculate_value(self):
        """
        Calculates the value of the hand.

        Returns:
            int: The total value of the hand.
        """
        self.value = sum([Deck().ranks[card[0]] for card in self.cards])
        self.adjust_for_ace()
        return self.value

    def adjust_for_ace(self):
        """
        Adjusts the value of the hand if an Ace is present and the total value exceeds 21.
        If there are Aces in the hand, it reduces the value of an Ace from 11 to 1 until the total value is less than or equal to 21.
        """
        self.aces = sum([1 for card in self.cards if card[0] == 'A'])
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
    def get_value(self):
        """
        Returns the value of the hand.

        Returns:
            int: The total value of the hand.
        """
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        """
        Checks if the hand is a blackjack.

        Returns:
            bool: True if the hand is a blackjack, False otherwise.
        """
        return self.get_value() == 21
    
    def display_hand(self, show_all_dealer_cards=False):
        """
        Displays the cards in the hand.

        Returns:
            None
        """
        print(f"{'Dealer' if self.dealer else 'Player'}'s Hand:")
        print(f"\t{Card(self.cards[0][0], self.cards[0][1])}")
        if not self.dealer or show_all_dealer_cards:
            for card in self.cards[1:]:
                print(f"\t{Card(card[0], card[1])}")
        else:
            print("\t<card hidden>")
        print(f"Total Value: {self.get_value()}")

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand(dealer=True)

    def start_game(self):
        """
        Starts the game by dealing cards to the player and dealer.

        Returns:
            None
        """
        self.player_hand.add_cards(self.deck.deal_card(2))
        self.dealer_hand.add_cards(self.deck.deal_card(2))
        self.player_hand.display_hand()
        self.dealer_hand.display_hand()

    def hit(self, hand):
        """
        Adds a card to the player's hand.

        Args:
            hand (Hand): The player's hand.

        Returns:
            None
        """
        hand.add_cards(self.deck.deal_card())

    def stand(self):
        """
        Ends the player's turn and starts the dealer's turn.

        Returns:
            None
        """
        self.dealer_hand.display_hand(show_all_dealer_cards=True)
        while self.dealer_hand.get_value() < 17:
            self.hit(self.dealer_hand)
            self.dealer_hand.display_hand(show_all_dealer_cards=True)
        self.check_winner()

    def check_winner(self):
        """
        Checks the winner of the game.

        Returns:
            None
        """
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        if player_value > 21:
            print("Player busts! Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busts! Player wins.")
        elif player_value == dealer_value:
            print("It's a tie!")
        elif player_value > dealer_value:
            print("Player wins!")
        else:
            print("Dealer wins!")


if __name__ == '__main__':
    game = Game()
    game.start_game()
    while game.player_hand.get_value() < 21:
        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            game.hit(game.player_hand)
            game.player_hand.display_hand()
        elif choice == 's':
            game.stand()
            break
        else:
            print("Invalid choice! Please enter 'h' or 's'.")
    else:
        print("Player busts! Dealer wins.")

