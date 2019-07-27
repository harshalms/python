import random  # to use Fisher Yates shuffle 
class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for val in [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(suit, val))
    def show(self):
        for i in self.cards:
            i.show()
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            random.shuffle(self.cards)
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def drawCard(self):
        # print(len(self.cards))
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self
    def showHand(self):
        for card in self.hand:
            card.show()
            
card = Card("Jack", 6)
# card.show()

deck = Deck()
# deck.show()
deck.shuffle()
# deck.show()
card = deck.drawCard()
# card.show()

bob = Player("Bob")
bob.draw(deck)
bob.showHand()