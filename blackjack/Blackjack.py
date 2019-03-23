from blackjack.Dealer import Dealer
from blackjack.Deck import Deck
from blackjack.Player import Player


class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        # Pass the player and the dealer two cards each
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

    def play(self):
        print("Player:\n", self.player)

        print("Dealer:\n", self.dealer)
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
                if self.player.hasBlackjack() and not self.dealer.hasBlackjack():
                    print("You win")
                elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():
                    print("Dealer wins")
                else:
                    print("There is a tie")

def main():
    game = Blackjack()
    game.play()

main()