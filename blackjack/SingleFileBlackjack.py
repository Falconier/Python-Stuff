##region File Info
# Jacob Emory Bullin
# SingleFileBlackjack.py
# 4/8/19
##endregion

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
        result += "\n " + str(self.getPoints()) + " points "
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

        self.Player = Player([self.deck.deal(), self.deck.deal()])
        self.Dealer = Dealer([self.deck.deal(),self.deck.deal()])

    def play(self):
        print("\nPlayer:\n", self.Player)
        print("Dealer:\n", self.Dealer)

        while True:
            choice = input("Would you like to hit enter yes or no: \n")
            if choice == "Yes" or choice =="yes" or choice =="y" or choice =="Y":
                self.Player.hit(self.deck.deal())
                points = self.Player.getPoints()
                print("Player: \n" , self.Player)
                if points >= 21:
                    break
            else:
                break

        playerPoints = self.Player.getPoints()
        if playerPoints > 21:
            print("You Busted")
        else:
            self.Dealer.hit(self.deck)
            print("Dealer\n", self.Dealer)
            dealerPoints = self.Dealer.getPoints()

            if dealerPoints > 21:
                print("\n Dealer Busted You Win!!! ")
            elif dealerPoints > playerPoints:
                print("Dealer Wins :O ")
            elif dealerPoints < playerPoints and playerPoints <= 21:
                print("\n You Win :D ")
            elif dealerPoints == playerPoints:
                if self.player.hasBlckjack() and not self.dealer.hasBlckjack():
                    print("\n you win :D ")
                elif not self.player.hasBlckjack() and self.dealer.hasBlckjack():
                    print("\n Dealer Wins")
                else:
                    print("\n There is a tie")


def main():
    again ="yes"
    while again == "Yes" or again =="yes" or again == "y" or again == "Y":
        print("-------------BlackJack------------")
        cardGame = Blackjack()
        cardGame.play()
        again = input("would you like to play again enter Yes or no: \n")

main()