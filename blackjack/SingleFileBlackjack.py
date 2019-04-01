import random


class Card:
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = self.rank
        return str(rank) + " of " + self.suit


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


class Player(object):
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        result = ", ".join(map(str, self.cards))
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
        Player.__init__(self, cards)
        self.showOneCard = True

    def __str__(self):
        if self.showOneCard:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())


class Blackjack(object):
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        # Pass the player and the dealer two cards each
        self.player = Player([self.deck.deal(),
        self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(),
        self.deck.deal()])
    def play(self):
        print("Player:\n", self.player)
        print("Dealer:\n", self.dealer)
        # Player hits until user says NO
        while True:
            choice = input("Do you want a hit? [y/n]: ")
            if choice in ("Y", "y"):
                self.player.hit(self.deck.deal())
                points = self.player.getPoints()
                print("Player:\n", self.player)
                if points >= 21:
                    break
            else:
                break
            playerPoints = self.player.getPoints()
            if playerPoints > 21:
                print("You bust and lose")
            else:
                # Dealer's turn to hit
                self.dealer.hit(self.deck)
                print("Dealer:\n", self.dealer)
                dealerPoints = self.dealer.getPoints()
                # Determine the outcome
                if dealerPoints > 21:
                    print("Dealer busts and you win")
                elif dealerPoints > playerPoints:
                    print("Dealer wins")
                elif dealerPoints < playerPoints and playerPoints <= 21:
                    print("You win")
                elif dealerPoints == playerPoints:
                    if self. player.hasBlackjack() and not self.dealer.hasBlackjack():
                        print("You win")
                    elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():
                        print("Dealer wins")
                    else:
                        print("There is a tie")


def main():
    game = Blackjack()
    game.play()


main()
