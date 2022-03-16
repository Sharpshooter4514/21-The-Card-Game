from time import sleep

class Players():

    def __init__(self):
        """Initializes a list that will contain our player name"""
        self.players = []
        
    def player_in_game_id(self):
        """Adds player ID's to a list"""
        sleep(1)
        player = input("Enter Player ID: \n>>> ")
        self.players.append(player)
        sleep(1)
        #print(self.players)
        return self.players


        