import random


class Deck:

    def __init__(self):
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
        self.deck = []

    def gen_cards(self):
        """Generates the deck of cards and stores it in a list"""
        for n in range(len(self.value)):
            for x in range(len(self.suit)):
                cards = self.value[int(n)] + " of " + self.suit[int(x)]
                self.deck.append(cards)
        return self.deck

    def count(self):
        """Shows numerical value of cards in deck"""
        return len(self.deck)

    def shuffle(self):
        """This function shuffles the cards"""
        random.shuffle(self.deck)
        return self.deck

    def card_values(self):
        """Sets the value of every card in the deck and puts it into a dictionary"""
        card_values = {}
        for x in range(len(self.deck)):
            #There are no ones in a deck of cards, the one in the case references the 10
            if self.deck[x][0] in ['K', 'Q', 'J', '1']:
                card_values[self.deck[x]] = 10
            elif self.deck[x][0] in ['2']:
                card_values[self.deck[x]] = 2
            elif self.deck[x][0] in ['3']:
                card_values[self.deck[x]] = 3
            elif self.deck[x][0] in ['4']:
                card_values[self.deck[x]] = 4
            elif self.deck[x][0] in ['5']:
                card_values[self.deck[x]] = 5
            elif self.deck[x][0] in ['6']:
                card_values[self.deck[x]] = 6
            elif self.deck[x][0] in ['7']:
                card_values[self.deck[x]] = 7
            elif self.deck[x][0] in ['8']:
                card_values[self.deck[x]] = 8
            elif self.deck[x][0] in ['9']:
                card_values[self.deck[x]] = 9
            elif self.deck[x][0] in ['A']:
                card_values[self.deck[x]] = 11
        return card_values
