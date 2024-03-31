import random

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(rank, suit) for suit in suits for rank in ranks]

def shuffle_deck(deck):
    random.shuffle(deck)
    
def deal_card(num_cards=1):
    return [deck.pop() for _ in range(num_cards)]

shuffle_deck(deck)
rank = deal_card(1)[0][0]
suit = deal_card(1)[0][1]
print(f'The card is the {rank} of {suit}')

if rank == 'A':
    value = 11
elif rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
    value = int(rank)
elif rank in ['J', 'Q', 'K']:
    value = 10
    
print(rank, value)