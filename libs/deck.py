"""Колода."""
from itertools import product

from libs.cards import Card
from config import VALUES, SUITS


class Deck:
    def __init__(self):
        self.cards = [Card(value, suit)
                      for value, suit in product(VALUES, SUITS)]
        self.shuffle_the_deck()
        self.trump_card = None
        self.get_trump_card()

    def __str__(self):
        return ', '.join([card.value for card in self.cards])

    def shuffle_the_deck(self):
        """Перемешать колоду."""

    def get_cards(self, count: int) -> list[Card]:
        """Выдать карты."""

    def is_empty(self) -> bool:
        """Проверяет, пуста ли кололда."""

    def get_trump_card(self):
        """Определить козырную карту."""
