"""Колода."""
from libs.cards import Card


class Stack:
    def __init__(self):
        nominal_values = ['6', '7', '8', '9', '10']
        suits = ['H', 'D', 'С', 'P']
        self.cards = []
        for nominal_value in nominal_values:
            for suit in suits:
                self.cards.append(Card(nominal_value, suit))

    def __str__(self):
        return ', '.join([card.value for card in self.cards])
