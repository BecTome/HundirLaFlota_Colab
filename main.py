from HLF.src.tablero import Tablero
from HLF.src.player import Player
import numpy as np

tablero_player = Tablero()
tablero_comp = Tablero()
tablero_comp_show = Tablero()

# Ininitialize boats
tablero_player.initialize_boats()
tablero_comp.initialize_boats()

player = Player("Alberto")
computer = Player("Computer")

while True:
    print("Player tablero:")
    print(tablero_player.tablero)
    print("Computer tablero:")
    print(tablero_comp_show.tablero)
    # Player shoot
    while True:
        print("\n")
        coord_x = int(input("Coord X: "))
        coord_y = int(input("Coord Y: "))
        try:
            tablero_comp.tablero = player.shoot(coord_x, coord_y, tablero_comp)
            tablero_comp_show.tablero = \
                    np.where((tablero_comp.tablero==Player.HIT_SIGN)|(tablero_comp.tablero==Player.WATER_SIGN), 
                                            tablero_comp.tablero, tablero_comp_show.tablero)
            if tablero_comp.tablero[coord_x, coord_y] == Player.HIT_SIGN:
                print("Hit")
                print(tablero_player.tablero)
                print(tablero_comp_show.tablero)
                continue
            else:
                print("Water")
                break
        except ValueError as e:
            print("You already shooted there")

    
    if ((tablero_comp.tablero == Player.HIT_SIGN).sum()\
            == np.sum(tablero_comp.BOAT_SIZES)):
        print(f"{player.name.upper()} wins")
        break

    # Computer shoot

    while True:
        coord_x_comp, coord_y_comp = np.random.randint(0, Tablero.SIZE, 2)
        try:
            tablero_player.tablero = computer.shoot(coord_x_comp, coord_y_comp, 
                                                    tablero_player)
            if tablero_player.tablero[coord_x, coord_y] == Player.HIT_SIGN:
                print("Hit")
                print(tablero_player.tablero)
                print(tablero_comp_show.tablero)
                continue
            else:
                print("Water")
                break
        except ValueError as e:
            continue
    # Check if someone wins
    
    if ((tablero_comp.tablero == Player.HIT_SIGN).sum()\
            == np.sum(tablero_player.BOAT_SIZES)):
        print(f"{computer.name.upper()} wins")
        break
