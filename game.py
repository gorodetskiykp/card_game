"""Точка входа в игру."""
from libs.deck import Deck


def main():
    """Основная логика игры."""
    print("Карточная игра")
    deck = Deck()
    print(deck)


if __name__ == '__main__':
    main()
