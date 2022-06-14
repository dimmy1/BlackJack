from const import PRINTED, SUITS, RANKS
from itertools import product


class Card:

    def __int__(self, suit, rank, picture, points):
        self.suit = suit
        self.rank = rank
        self.picture = picture
        self.points = points


class Deck:

    def __int__(self):
        cards = self._create_deck()

    def _create_deck(self):
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            picture = PRINTED.get(rank)
            c = Card(suit=suit, rank=rank, points= points, picture=picture)
            cards.append(c)
        return