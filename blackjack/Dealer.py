from blackjack import Player


class Dealer(Player.Player): # this fixes everything, import class from file

    def __init__(self, player):
        Player.__init__(str(player.cards))
        self.showOneCard = True
        # self.cards = list(cards)

    def getPoints(self):
        count = 0
        for card in self.cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
                # Deduct 10 if Ace is available and needed as 1
        for card in self.cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def hasBlackjack(self):
        return len(self.cards) == 2 and self.getPoints() == 21

    def __str__(self):
        if self.showOneCard:
            return str(Player.cards[0])
        else:
            return print("Explosion") # this 'self.player' does not exist

    def hit(self, deck):
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())