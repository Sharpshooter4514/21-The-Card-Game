import random

class Deck():
    
    def __init__(self):
       self.value = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
       self.suit = ["Spades","Hearts","Diamonds","Clubs"]
       
    def gen_cards(self):
        """Generates the deck of cards and stores it in a list"""
        self.deck = []
        for n in range(13):
            for l in range(4):
                cards = self.value[n] + " of " + self.suit[l]
                self.deck.append(cards)
        return self.deck
         
    def count(self):
        """Shows numerical value of cards in deck"""
        return len(self.deck)
    
    def shuffle(self):
        """This function shuffles the cards"""
        deck = self.deck
        random.shuffle(deck)
        return deck
    