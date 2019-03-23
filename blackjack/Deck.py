##region File Information
# Deck class
# Deck.py
# Jacob Emory Bullin
##endregion

##region Imports
from blackjack.Cards import Card
import random
##endregion

class Deck:


    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self) == 0:
            return None
        else:
            return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        result = ""
        for c in self.cards:
            result = result + str(c) + '\n'
        return result

# def main():
#     d = Deck()
#     print(d)
#
# main()