"""Проверка функции get_trump_card."""
from itertools import product

from config import VALUES, SUITS
from libs.cards import Card
from random import choice


trump_card = None

cards = [Card(value, suit) for value, suit in product(VALUES, SUITS)]

if trump_card is None:
    trump_card = choice(cards)
    while True:
        if 'A' in str(trump_card):
            trump_card = choice(cards)
        else:
            break
    cards.remove(trump_card)
    cards.append(trump_card)

print(trump_card)

print(cards)