import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        self.board = self.make_new_board()
        self.assign_values_to_board()

        self.dug = set()

    def make_new_board(self):
     
        return [] # change this

    def assign_values_to_board(self):

        pass

    def get_num_neighboring_bombs(self, row, col):
   

        # ps we need to make sure we don't go out of bounds!!
        pass

    def dig(self, row, col):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a couple of scenarios to consider:
        # hit a bomb -> game over
        # dig at a location with neighboring bombs -> finish dig
        # dig at a location with no neighboring bombs -> recursively dig neighbors!
        pass

    def __str__(self):
        # return a string that shows the board to the player
        # note: this part is kinda hard to get the formatting right, you don't have to do it the same way
        # i did
        # you can also just copy and paste from the implementation
        # this part is not that important to understanding the logic of the code :)
        return ''

def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if the location is a bomb, then show game over message
    # Step 3b: if the location is not a bomb, dig recursively until one of the squares is next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig, then show victory
    pass

if __name__=='__main__':
    play()
    
