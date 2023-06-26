import os, sys
sys.path.append(os.getcwd())
from HLF.utils import config

class Player():
    HIT_SIGN = config.HIT_SIGN    
    WATER_SIGN = config.WATER_SIGN

    def __init__(self, name):
        self.name = name

    def shoot(self, coord_x, coord_y, tablero):
        '''
        Shoot to the board
        '''
        coord = (coord_x, coord_y)
        tab = tablero.tablero.copy()
        if tab[coord] == tablero.BOAT_SIGN:
            tab[coord] = self.HIT_SIGN
            # self.tablero.tablero = tab
        elif tab[coord] == tablero.EMPTY_SIGN:
            tab[coord] = self.WATER_SIGN
            # self.tablero.tablero = tab
        elif tab[coord] == self.HIT_SIGN or tab[coord] == self.WATER_SIGN:
            raise ValueError("You already shooted there")

        return tab
    
if __name__ == "__main__":
    from HLF.src.tablero import Tablero
    tablero_to_shoot = Tablero()
    tablero_to_shoot.initialize_boats()
    player = Player("Player 1")
    print(player)