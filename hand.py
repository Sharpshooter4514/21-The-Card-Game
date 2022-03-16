from deck import Deck

class Hand():
    
    def __init__(self):
        d = Deck()
        d.gen_cards()
        self.deck = d.shuffle()
        
    def gen_hand(self):
        """This generates the cards for everyones hand in the form of a list"""
        # This deck attribute should inherit from the shuffle function
        num2 = int(1) * 2 + 2
        gen_hand = []
        for x in range(int(num2)):
            gen_hand.append(self.deck.pop())
        return gen_hand
    
    def distribute_hand(self, hand, player):
        """Splits and distributes the hands"""
        self.player = player
        self.player_hand = hand[0:2]
        self.computer_hand = hand[2:4]
        
        
    def hit_or_stay(self):
        choice = input("Would you like to hit or stay (h/s)").lower()
        if choice in ["hit","h"]:
            print("You chose hit:")
        elif choice in ["stay","s"]:
            print("You chose stay")
        
            