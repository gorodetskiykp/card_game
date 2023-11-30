"""Игрок."""
from libs.cards import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self._cards = []

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
