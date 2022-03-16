from deck import Deck
from players import Players
from hand import Hand
import random

p = Players()
player = p.player_in_game_id()

h = Hand()
hand = h.gen_hand()
h.distribute_hand(hand, player)



