

class Player:

    def __init__(self, cards):
        self.cards = list(cards)

    def __str__(self):
        # result = ", ".join(map(str, self.cards))
        result = ""
        for i in self.cards:
            result += i.__str__()
        result += "\n " + str(self.getPoints()) + " points"
        return result

    def hit(self, card):
        self.cards.append(card)

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

class Dealer(Player):

    def __init__(self, cards):
        Player.__init__(self,cards)
        self.showOneCard = True

    def __str__(self):
        if self.showOneCard:
            return str(Player.cards[0])
        else:
            return print("Explosion") # this 'self.player' does not exist
    def hit(self, deck):
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())
