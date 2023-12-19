from libs.deck import Deck
from libs.players import Player


class Match:
    def __init__(self, *players: str):
        self.deck = Deck()
        self.players = [Player(name) for name in players]
