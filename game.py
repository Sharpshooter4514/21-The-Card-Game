from deck import Deck
from players import Players
from hand import Hand
import time

'''
class ai:
    def __init__(self):
        self.ai_hand = []

    def ai_move(self):
'''

player_stays = False
ai_stays = False
d = Deck()
p = Players()
player = p.player_in_game_id()

print("")

h = Hand()
hand = h.gen_hand()
c_deck = hand[1]
hand = hand[0]

dis_hands = h.distribute_hand(hand, player)

#Seperate the hands from the list so they can be used in the program
player_hand = []
ai_hand = []
player_hand.append(dis_hands[0][0])
player_hand.append(dis_hands[0][1])
ai_hand.append(dis_hands[1][0])
ai_hand.append(dis_hands[1][1])

def player_turn(hnd, dictply):
    """
    :param hnd: This is the current hand as it has been added to throughout the course of the game.
    :param dictply: This is the dictionary that stores the value of each card as an integer.
    :return:
    """
    player_turn.player_stays = False
    d = dictply
    num1 = 0
    player_turn.hnd = hnd
    choice = input("Would you like to hit or stay (h/s): \n>>> ").lower()
    if choice in ['hit', 'h']:
        player_turn.draw = h.hit_or_stay()
        drawn_card = player_turn.draw[0]
        player_turn.hnd.append(drawn_card)
        for x in range(len(hnd)):
            num = d.get(hnd[x])
            num1 = num + num1
            if num1 == 21:
                time.sleep(0.7)
                print("You have won the game!")
                time.sleep(4)
                exit()
            elif num1 > 21:
                time.sleep(0.7)
                print("You have lost the game, you're hand exceeds 21...")
                time.sleep(4)
                exit()
    elif choice in ['stay', 's']:
        print('You have chosen to stay...')
        time.sleep(0.7)
        player_turn.player_stays = True
    else:
        print('Not a valid input')

def show_new_hand(player_hand_new):
    """
    :param player_hand_new: This function inherits the current hand of the player.
    :return:
    """
    for i in player_hand_new:
        print(i)

def ai_turn(ai_hand_func, dictai, cdeck):
    ai_turn.ai_stays = False
    ai_turn.new_aihand = ai_hand_func
    d = dictai
    ai_turn.cdeck = cdeck
    num1 = 0
    for x in range(len(ai_turn.new_aihand)):
        num = d.get(ai_turn.new_aihand[x])
        num1 = num + num1
        if num1 == 21:
            print("Computer has won the game.")
            time.sleep(4)
            exit()
        elif num1 > 21:
            print("Computers score exceeded 21, you have won the game!")
            time.sleep(4)
            exit()
    if num1 >= 16:
        print("A.I. has chosen to stay...")
        ai_turn.ai_stays = True
    elif num1 < 16:
        print("A.I. chooses to hit...")
        ai_turn.new_deck = ai_turn.cdeck.pop()
        ai_turn.new_aihand.append(ai_turn.new_deck)

#Generates the deck of cards and each one is assigned its value. Values are stored in a dictionary
d.gen_cards()
card_dict = d.card_values()

#Show the player their hand
print(player[0] + ', your hand is: ')
for x in player_hand:
    print('    ' + x)
time.sleep(0.5)

while player_stays is False or ai_stays is False:
    #Players turn
    player_turn(player_hand, card_dict)
    player_stays = player_turn.player_stays

    #Get the current deck out of function player_turn
    if player_stays is True:
        pass
    elif player_stays is False:
        c_deck = player_turn.draw[1]
    print("")

    #A.I. turn
    ai_turn(ai_hand, card_dict, c_deck)
    ai_stays = ai_turn.ai_stays
    print("")

    #Get current deck and hand for A.I. out of ai_turn fucntion
    ai_hand = ai_turn.new_aihand
    c_deck = ai_turn.cdeck

print('Both you and your opponent have stayed:')
print('Your hand:')
for i in player_turn.hnd:
    print('    ' + i)
print('A.I. Hand:')
for i in ai_hand:
    print('    ' + i)

player_total = 0
for x in range(len(player_turn.hnd)):
    num = card_dict.get(player_turn.hnd[x])
    player_total = num + player_total

ai_total = 0
for x in range(len(ai_hand)):
    num = card_dict.get(ai_hand[x])
    ai_total = num + ai_total

if player_total > ai_total:
    print(player[0] + ' ,you have won the game!')
    time.sleep(4)
    exit()
elif ai_total > player_total:
    print(player[0] + ' , you have lost the game...')
    time.sleep(4)
    exit()
else:
    print('Tie!')
    time.sleep(4)
    exit()








