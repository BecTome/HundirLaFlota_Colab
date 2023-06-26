import os, sys
import numpy as np
sys.path.append(os.getcwd())

from HLF.src.tablero import Tablero

def test_init_size():
    size = 6
    tablero = Tablero(size)
    shape_cond = tablero.tablero.shape == (size, size)
    assert shape_cond

def test_place_boat_size_3_inside_board_size_5():
    size = 5
    boat_size = 3
    orig = (2, 2)
    tablero = Tablero(size=size)
    e = tablero.EMPTY_SIGN
    b = tablero.BOAT_SIGN

    arr_comp_S = np.array([[e, e, e, e, e],
                           [e, e, e, e, e],
                           [e, e, b, e, e],
                           [e, e, b, e, e],
                           [e, e, b, e, e]])
    
    arr_comp_N = np.array([[e, e, b, e, e],
                           [e, e, b, e, e],
                           [e, e, b, e, e],
                           [e, e, e, e, e],
                           [e, e, e, e, e]])
    
    arr_comp_E = np.array([[e, e, e, e, e],
                           [e, e, e, e, e],
                           [e, e, b, b, b],
                           [e, e, e, e, e],
                           [e, e, e, e, e]])

    arr_comp_W = np.array([[e, e, e, e, e],
                           [e, e, e, e, e],
                           [b, b, b, e, e],
                           [e, e, e, e, e],
                           [e, e, e, e, e]])
    
    cond_S = np.all(tablero.place_boat(orig, "S", boat_size) == arr_comp_S)
    cond_N = np.all(tablero.place_boat(orig, "N", boat_size) == arr_comp_N)
    cond_E = np.all(tablero.place_boat(orig, "E", boat_size) == arr_comp_E)
    cond_W = np.all(tablero.place_boat(orig, "W", boat_size) == arr_comp_W)

    assert cond_S and cond_N and cond_E and cond_W

def test_valid_condition_border_size_3_inside_board_size_5():

    size = 5
    boat_size = 3
    tablero = Tablero(size=size)

    # Invalid positions for the north orientation
    orig = (0, 0)
    cond_N = tablero.valid_position(orig, "N", boat_size)
    assert not cond_N

    # Invalid positions for the south orientation
    orig = (3, 0)
    cond_S = tablero.valid_position(orig, "S", boat_size)
    assert not cond_S

    # Invalid positions for the east orientation
    orig = (0, 3)
    cond_E = tablero.valid_position(orig, "E", boat_size)
    assert not cond_E

    # Invalid positions for the west orientation
    orig = (0, 0)
    cond_W = tablero.valid_position(orig, "W", boat_size)
    assert not cond_W

def test_valid_condition_overlap_size_3_inside_board_size_5():

    size = 5
    boat_size = 3
    orig = (2, 2)
    tablero = Tablero(size=size)
    tablero.tablero[:, :] = tablero.BOAT_SIGN

    # Overlapping for the north orientation
    cond_N = tablero.valid_position(orig, "N", boat_size)
    assert not cond_N

    # Overlapping for the south orientation
    cond_S = tablero.valid_position(orig, "S", boat_size)
    assert not cond_S

    # Overlapping for the east orientation
    orig = (0, 3)
    cond_E = tablero.valid_position(orig, "E", boat_size)
    assert not cond_E

    # Overlapping for the west orientation
    orig = (0, 0)
    cond_W = tablero.valid_position(orig, "W", boat_size)
    assert not cond_W

def test_initialize_boats():
    size = 5
    tablero = Tablero(size=size)
    tablero.BOAT_SIZES = [3, 2, 1]
    tablero.initialize_boats()
    assert np.sum(tablero.tablero == tablero.BOAT_SIGN) == np.sum(tablero.BOAT_SIZES)