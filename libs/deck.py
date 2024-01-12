"""Колода."""
from itertools import product

import self

from libs.cards import Card
from config import VALUES, SUITS
from random import choice, shuffle

class Deck:
    def __init__(self):
        self.cards = [Card(value, suit)
                      for value, suit in product(VALUES, SUITS)]
        self.trump_card = None

        self.shuffle_the_deck()
        self.get_trump_card()

    def __str__(self):
        return ', '.join([card.value for card in self.cards])

    def shuffle_the_deck(self):
        """Перемешать колоду."""
        shuffle(self.cards)

    def get_cards(self, count: int) -> list[Card]:
        """Выдать карты."""

    def is_empty(self) -> bool:
        """Проверяет, пуста ли кололда."""
        return len(self.cards) == 0

    def get_trump_card(self):
        """Определить козырную карту."""
        if self.trump_card is None:
            self.trump_card = choice(self.cards)
            while True:
                if 'A' in str(self.trump_card):
                    self.trump_card = choice(self.cards)
                else:
                    break
            self.cards.remove(self.trump_card)
            self.cards.append(self.trump_card)
