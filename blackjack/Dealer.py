from blackjack import Player


class Dealer:

    def __init__(self, cards):
        Player.__init__(cards)
        self.showOneCard = True

    def __str__(self):
        if self.showOneCard:
            return str(self.cards[0])
        else:
            return print(self.player)
    def hit(self, deck):
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())
