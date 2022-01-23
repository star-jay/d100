# from wfc.constants import (UP, DOWN, RIGHT, LEFT)
from wfc.wfc import wfc
from wfc.utils import eight_versions


# Test entire wfc flow
def test_wfc():
    W, L, R = range(3)
    # N = 2
    tiles = [
        [
            [W, W],
            [W, L],
        ],
    ]

    patterns = []
    for tile in tiles:
        patterns += eight_versions(tile)

    wfc(patterns, 16)


# Test entire wfc flow
def test_wfc_3():
    W, L, R = range(3)
    # N = 2
    tiles = [
        [
            [W, W, W],
            [W, L, L],
            [W, L, L],
        ],
        [
            [W, W, W],
            [W, W, L],
            [W, L, L],
        ],
    ]

    patterns = []
    for tile in tiles:
        patterns += eight_versions(tile)

    wfc(patterns, 16)
