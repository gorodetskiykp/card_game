"""Колода."""
from itertools import product

from libs.cards import Card
from config import VALUES, SUITS


class Deck:
    def __init__(self):
        self.shuffled = None
        self.cards = [Card(value, suit)
                      for value, suit in product(VALUES, SUITS)]
        self.trump_card = None

        self.shuffle_the_deck()
        self.get_trump_card()

    def __str__(self):
        return ', '.join([card.value for card in self.cards])

    def shuffle_the_deck(self):
        """Перемешать колоду."""
        self.shuffled = True

    def get_cards(self, count: int) -> list[Card]:
        """Выдать карты."""
        hand_add = []
        if len(self.cards) >= count:  # определяет сколько карт может раздать
            number_of_cards = count
        else:
            number_of_cards = len(self.cards)
        if self.trump_card is not None and self.shuffled:
            if self.is_empty is True:
                print('Ошибка раздачи карт, колода кончилась!')
            else:
                hand_add = self.cards[:number_of_cards]
                del self.cards[:number_of_cards]
        else:
            print('Козырь не определен ли колода не перемешана')
        return hand_add

    def is_empty(self) -> bool:
        """Проверяет, пуста ли кололда."""
        return len(self.cards) == 0

    def get_trump_card(self):
        """Определить козырную карту."""
