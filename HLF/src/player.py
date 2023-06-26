import os, sys
sys.path.append(os.getcwd())
from HLF.utils import config

class Player():
    HIT_SIGN = config.HIT_SIGN    
    WATER_SIGN = config.WATER_SIGN

    def __init__(self, name, tablero):
        self.name = name
        self.tablero = tablero

    def shoot(self, coord):
        '''
        Shoot to the board
        '''
        tab = self.tablero.tablero.copy()
        if tab[coord] == self.tablero.BOAT_SIGN:
            tab[coord] = self.HIT_SIGN
            # self.tablero.tablero = tab
        elif tab[coord] == self.tablero.EMPTY_SIGN:
            tab[coord] = self.WATER_SIGN
            # self.tablero.tablero = tab
        elif tab[coord] == self.HIT_SIGN or tab[coord] == self.WATER_SIGN:
            raise ValueError("You already shooted there")

        return tab
    
if __name__ == "__main__":
    from HLF.src.tablero import Tablero
    tablero_player = Tablero()
    player = Player("Player 1", tablero_player)
    print(player)