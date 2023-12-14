from deck import Deck
from players import Player

class Match:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player('1'), Player('2')]
