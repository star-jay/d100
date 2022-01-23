from wfc.constants import (UP, DOWN, RIGHT, LEFT)
from wfc.wfc import get_neighbours


def test_remove_invalid_options():
    neighbours = get_neighbours(1, 1, 3)
    assert neighbours[UP] == (1, 0)
    assert neighbours[DOWN] == (1, 2)
    assert neighbours[LEFT] == (0, 1)
    assert neighbours[RIGHT] == (2, 1)
