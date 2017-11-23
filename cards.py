from random import randint

class PlayingCard(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        self.index = randint(0,1000)

    def __str__(self):
        return "(" + str(self.value) + " of " + str(self.suit) + ")"

    __repr__ = __str__


class Deck(object):
    def __init__(self):
        self.cards = []
        for i in range(0,4):
            for j in range(1,14):
                if i == 0:
                    self.cards.append(PlayingCard("♠",j))
                elif i == 1:
                    self.cards.append(PlayingCard("♣",j))
                elif i == 2:
                    self.cards.append(PlayingCard("♥",j))
                else:
                    self.cards.append(PlayingCard("♦",j))

    def __str__(self):
        return "There are " + str(len(self.cards)) + " cards in the deck."

    def readCards(self):
        print(self.cards)

    def shuffle(self):
        self.cards.sort(key=lambda cards: cards.index, reverse=False)
        return self.cards

    def deal(self,numberOfCards):
        hand = []
        for i in range(0,numberOfCards):
            hand.append(self.cards.pop())
        return hand



deck = Deck()
print(deck)
print(deck.shuffle())

hand =  deck.deal(5)
print("\nPlayer Hand: " + str(hand))