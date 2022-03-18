from deck import Deck
from players import Players
from hand import Hand
import time


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

# Separate the hands from the list so they can be used in the program
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
    dictcards = dictply
    num1 = 0
    player_turn.hnd = hnd
    choice = input("Would you like to hit or stay (h/s): \n>>> ").lower()
    if choice in ['hit', 'h']:
        player_turn.draw = h.hit_or_stay()
        drawn_card = player_turn.draw[0]
        player_turn.hnd.append(drawn_card)
        for x in range(len(hnd)):
            num = dictcards.get(hnd[x])
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
    """
        :param ai_hand_func: These are the two cards that have been drawn for the ai
        :param dictai: Dictionary that contains the entire deck of cards. Key is name of card, value is int that
                       represents the numeric value of the card.
        :param cdeck: Dictionary that contains the deck of cards minus the cards that have been drawn between the
                      players and ai.
        :return:
        """
    ai_turn.ai_stays = False
    ai_turn.new_aihand = ai_hand_func
    d = dictai
    ai_turn.cdeck = cdeck
    num1 = 0
    prob_arry = []

    for i in ai_turn.cdeck:
        # This loop takes all of the cards un-drawn from the deck and converts them to an array of integers
        prob_arry.append(int(d[i]))
    tnumleft = len(prob_arry)

    # These s values represent a group for each numerical category of card s1 will be all of the 2's s2 all of the 3's..
    values_left_deck = {}

    # Dictionary to hold variables for numerical count of cards left in deck
    initdict = {}
    # Array to simplify writing out the key values of s1-s10 for initdict{}
    intodict =[]

    # Creates the name for all of the variables that will be used in a dictionary as keys.
    x = 2
    while x < 12:
        intodict.append('s' + str(x))
        x = int(x) + 1

    # Adds the value of 0 to all of the keys in initdict{}
    for i in intodict:
        initdict[i] = 0

    '''
    The loop below this will take all of the numeric values from the prob_arry and loop through all of the possible
    values for each card that could be left in the deck. Those values can range from 2-11.
    '''
    x = 2
    cont = 0
    # Every time this while loop reset the value of x will increase by one. Goes values 2-11
    while cont < 10:
        for i in prob_arry:
            if i == x:
                val = initdict['s' + str(x)]
                val = val + 1
                initdict['s' + str(x)] = val
        cont = cont + 1
        x = x + 1

    # For loop calculate the probability for each possible value that could be drawn from the existing deck of cards.
    for key in initdict:
        initdict[key] = (initdict[key]/tnumleft) * 100

    # This bit of code calculates how many points are needed to win.
    c_val = 0
    c_valneeded = 0
    for i in ai_turn.new_aihand:
        c_val = c_val + dictai[i]
    c_valneeded = 21 - c_val
    # print('c_val:', c_val, 'c_valneeded:', c_valneeded)


    # Calculates the probability of drawing the needed card.
    x = 2
    percnt = 0
    while x <= c_valneeded and x <= 11:
        percnt = percnt + initdict['s' + str(x)]
        x = x + 1
    print('Probability of drawing card less than: ', c_valneeded, ' is: ', percnt)

    # This for loop will ensure that if the computers hand is precisely 21 it automatically wins.
    for x in range(len(ai_turn.new_aihand)):
        num = d.get(ai_turn.new_aihand[x])
        num1 = num + num1
        if num1 == 21:
            print("Computer has won the game.")
            time.sleep(4)
            exit()

    if percnt > 35:
        print("A.I. chooses to hit...")
        ai_turn.new_deck = ai_turn.cdeck.pop()
        ai_turn.new_aihand.append(ai_turn.new_deck)
        tot_val = 0
        for i in ai_turn.new_aihand:
            tot_val = tot_val + dictai[i]
        if tot_val > 21:
            print('Computers hand is larger than 21, you have won the game.')
            exit()
    elif percnt < 0:
        print("Computers score exceeded 21, you have won the game!")
        time.sleep(2)
        exit()
    else:
        print("A.I. has chosen to stay...")
        ai_turn.ai_stays = True

# Generates the deck of cards and each one is assigned its value. Values are stored in a dictionary
d.gen_cards()
card_dict = d.card_values()

# Show the player their hand
vf = 0
print(player[0] + ', your hand is: ')
for x in player_hand:
    print('    ' + x)
for i in player_hand:
    vf = vf + card_dict[i]
    if vf == 21:
        print('Player has won the game with a score of 21!')
        time.sleep(2)
        exit()

while player_stays is False or ai_stays is False:
    # While this loop is active, as long as either player_stays or ai_stays remains false, the loop will continue.
    # Players turn
    player_turn(player_hand, card_dict)
    player_stays = player_turn.player_stays

    # Get the current deck out of function player_turn
    if player_stays is True:
        pass
    elif player_stays is False:
        c_deck = player_turn.draw[1]
    print("")

    # A.I. turn
    ai_turn(ai_hand, card_dict, c_deck)
    ai_stays = ai_turn.ai_stays
    print("")

    # Get current deck and hand for A.I. out of ai_turn function
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








