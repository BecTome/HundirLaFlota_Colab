import os, sys
import numpy as np
sys.path.append(os.getcwd())

from HLF.src.tablero import Tablero
from HLF.src.player import Player

def test_shoot_hit():
    tablero = Tablero(size=5)
    player = Player("Player 1")
    coord = (2, 2)
    tablero.tablero[coord] = tablero.BOAT_SIGN
    tablero.tablero = player.shoot(coord[0], coord[1], tablero)
    assert tablero.tablero[coord] == player.HIT_SIGN

def test_shoot_water():
    tablero = Tablero(size=5)
    player = Player("Player 1")
    coord = (0, 0)
    tablero.tablero[coord] = tablero.EMPTY_SIGN
    tablero.tablero = player.shoot(coord[0], coord[1], tablero)
    assert tablero.tablero[coord] == player.WATER_SIGN

def test_shoot_already_shooted():
    tablero = Tablero(size=5)
    player = Player("Player 1")
    coord = (0, 0)
    tablero.tablero = player.shoot(coord[0], coord[1], tablero)
    try:
        tablero.tablero = player.shoot(coord[0], coord[1], tablero)
    except ValueError:
        assert True
    else:
        assert False