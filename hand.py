import time

from deck import Deck

class Hand:
    
    def __init__(self):
        d = Deck()
        d.gen_cards()
        self.deck = d.shuffle()
        
    def gen_hand(self):
        """This generates the cards for everyones hand in the form of a list"""
        # This deck attribute should inherit from the shuffle function in deck.py
        num2 = int(1) * 2 + 2
        gen_hand = []
        for x in range(int(num2)):
            gen_hand.append(self.deck.pop())
        return gen_hand, self.deck
    
    def distribute_hand(self, hand, player):
        """Splits and distributes the hands"""
        self.player = player
        self.player_hand = hand[0:2]
        self.computer_hand = hand[2:4]
        return self.player_hand, self.computer_hand

    def hit_or_stay(self):
        deck_pop = self.deck.pop()
        time.sleep(0.7)
        print("")
        print("You chose hit, here is your new card:")
        #print(len(self.deck))
        print('    ' + deck_pop)
        return deck_pop, self.deck


        
            