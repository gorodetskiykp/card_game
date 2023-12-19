from deck import Deck
from players import Player


class Match:
    def __init__(self, *players: tuple[str]):
        self.deck = Deck()
        self.players = [Player(name) for name in players]
