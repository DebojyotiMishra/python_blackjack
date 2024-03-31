# Blackjack Game

This is a simple implementation of the Blackjack card game in Python.

## How to Play

1. Run the `main.py` file to start the game.
2. The game will deal two cards to the player and two cards to the dealer.
3. The player's hand will be displayed, showing one of the dealer's cards.
4. The player can choose to either "hit" (receive another card) or "stand" (end their turn).
5. If the player's hand value exceeds 21, they bust and the dealer wins.
6. Once the player stands, the dealer will reveal their hidden card and continue drawing cards until their hand value is at least 17.
7. If the dealer's hand value exceeds 21, they bust and the player wins.
8. The winner is determined by comparing the hand values. If the values are equal, it's a tie.

## Classes

### Card

Represents a playing card with a rank and suit.

### Deck

Represents a deck of cards. It can be shuffled and cards can be dealt from it.

### Hand

Represents a player's or dealer's hand. It can receive cards, calculate the hand value, adjust for aces, and display the hand.

### Game

Controls the flow of the game. It initializes the deck and hands, starts the game, handles player actions, and determines the winner.

## How to Contribute

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.
