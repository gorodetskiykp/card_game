"""Карты."""


class Card:
    def __init__(self, nominal_value, suit):
        self.nominal_value = nominal_value
        self.suit = suit
        self.value = nominal_value + suit

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
