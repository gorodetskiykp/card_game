"""Точка входа в игру."""
from libs.deck import Deck
from libs.match import Match
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
    game = Match('P1', 'P2')
    print(game.players)


if __name__ == '__main__':
    main()
