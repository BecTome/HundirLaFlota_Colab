import numpy as np
import os, sys
sys.path.append(os.getcwd())
from HLF.utils import config

class Tablero:
    # Constants (Class attributes)
    SIZE = config.SIZE
    EMPTY_SIGN = config.EMPTY_SIGN
    BOAT_SIGN = config.BOAT_SIGN
    BOAT_SIZES = config.BOAT_SIZES

    def __init__(self, size=None):
        '''
        Initialize the board with the given size.

        Parameters
        ----------
        size : int, optional
            Size of the board. The default is None.
        '''
        # If size is not given, use the default value
        if size is not None:
            self.SIZE = size
        
        # Initialize the board with the given size and fill it with empty signs
        self.tablero = np.full(shape=(self.SIZE, self.SIZE), 
                               fill_value=self.EMPTY_SIGN)
    
    def __clear_(self):
        '''
        Clear the board before placing the boats.
        '''
        self.tablero = np.full(shape=(self.SIZE, self.SIZE), 
                               fill_value=self.EMPTY_SIGN)

    def initialize_boats(self):
        '''
        Initialize the boats in the board.
        Use the BOAT SIZES and the possible orientations to place the boats.
        '''
        self.__clear_()
        ls_orients = ["N", "S", "E", "W"]
        for boat_size in self.BOAT_SIZES:
            while True:
                # take random origin and orientation
                orig = np.random.randint(0, self.SIZE, size=2)
                orient = np.random.choice(ls_orients)
                try:
                    # try to place the boat checking if the position is valid
                    self.tablero = self.place_boat(orig, orient, boat_size)
                    break
                except ValueError:
                    # Otherwise, continue trying
                    pass
    
    def place_boat(self, orig, orient, boat_size):
        '''
        Place a boat of size `boat_size` in the board given 
        origin and orientation.
        '''

        # Copy the board to avoid modifying the original board
        tab = self.tablero.copy()
        orig_row, orig_col = orig

        # Check if the position is valid
        cond = self.valid_position(orig, orient, boat_size)
        if cond:
            # In case it's valid, place the boat depending on the orientation
            if orient == "N":
                # final_row is the row of the last position of the boat
                # As it grows to the north, it's lower than the origin
                final_row = orig_row - (boat_size - 1)
                tab[final_row:(orig_row + 1), orig_col] = self.BOAT_SIGN
            elif orient == "S":
                # final_row is the row of the last position of the boat
                # As it grows to the south, it's higher than the origin
                final_row = orig_row + (boat_size - 1)
                tab[orig_row:(final_row + 1), orig_col] = self.BOAT_SIGN
            elif orient == "E":
                # final_col is the column of the last position of the boat
                # As it grows to the east, it's higher than the origin
                final_col = orig_col + (boat_size - 1)
                tab[orig_row, orig_col:(final_col + 1)] = self.BOAT_SIGN
            elif orient == "W":
                # final_col is the column of the last position of the boat
                # As it grows to the west, it's lower than the origin
                final_col = orig_col - (boat_size - 1)
                tab[orig_row, final_col:(orig_col + 1)] = self.BOAT_SIGN
            return tab
        else:
            raise ValueError("Invalid position")
        
    
    def valid_position(self, orig, orient, boat_size):
        '''
        Check if the position is valid.
        We say a position is valid if:
            - The boat doesn't go out of the board
            - The boat doesn't overlap with another boat
        '''
        orig_row, orig_col = orig
        if orient == "N":
            final_row = orig_row - (boat_size - 1)
            # Check if the final row (lower in this case) is greater than 0
            # We know the higher is lower than the size because we will use
            # bounded random numbers
            cond_border = final_row >= 0
            cond_overlap = np.any(self.tablero[final_row:(orig_row + 1), orig_col] == self.BOAT_SIGN)
        elif orient == "S":
            # Check if the final row (higher in this case) is lower than the size
            # We know the lower is greater 0 because we will use
            # bounded random numbers from 0 to size - 1
            final_row = orig_row + (boat_size - 1)
            cond_border = final_row < self.SIZE
            cond_overlap = np.any(self.tablero[orig_row:(final_row + 1), orig_col] == self.BOAT_SIGN)
        elif orient == "E":
            # Check if the final row (higher in this case) is lower than the size
            # We know the lower is greater 0 because we will use
            # bounded random numbers from 0 to size - 1
            final_col = orig_col + (boat_size - 1)
            cond_border = final_col < self.SIZE
            cond_overlap = np.any(self.tablero[orig_row, orig_col:(final_col + 1)] == self.BOAT_SIGN)
        elif orient == "W":
            # Check if the final row (lower in this case) is greater than 0
            # We know the higher is lower than the size because we will use
            # bounded random numbers
            final_col = orig_col - (boat_size - 1)
            cond_border = final_col >= 0
            cond_overlap = np.any(self.tablero[orig_row, final_col:(orig_col + 1)] == self.BOAT_SIGN)
        return cond_border and not cond_overlap

        

if __name__ == "__main__":
    tablero_player = Tablero()
    print(tablero_player.SIZE)