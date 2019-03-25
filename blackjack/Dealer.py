from blackjack import Player


class Dealer(Player):

    def __init__(self, cards):
        Player.__init__(self,cards)
        self.showOneCard = True

    def __str__(self):
        if self.showOneCard:
            return str(super().cards[0])
        else:
            return print("Explosion") # this 'self.player' does not exist
    def hit(self, deck):
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())
