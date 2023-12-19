"""Игрок."""
from libs.cards import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self._cards: list[Card] = []

    @property
    def cards(self):
        """Вернуть карты игрока."""
        if self._cards:
            return ', '.join(self._cards)
        else:
            return "Пусто"
    
    def receive_cards(self, cards: list[Card]):
        """Принять карты и добавить их к картам игрока."""
        self._cards.extend(cards)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
