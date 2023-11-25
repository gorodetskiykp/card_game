"""Игрок"""
from libs.cards import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.player_cards = [] 

    def show_cards(self):
        """возвращает карты игрока"""
        return self.player_cards
    
    def receive_cards(self, cards):
        """Принимает карты и добавляет их к картам игрока"""
        self.player_cards.extend(cards) 