"""Точка входа в игру."""
from libs.deck import Deck
from libs.players import Player


def main():
    """Основная логика игры."""
    print("Карточная игра")
    deck = Deck()
    print(deck)
    players = [
        Player("P1"),
        Player("P2"),
    ]
    for player in players:
        print('{:<10}: {}'.format(player.name, player.cards))


if __name__ == '__main__':
    main()
