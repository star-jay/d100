# from d100.wcf.constants import (UP, DOWN, RIGHT, LEFT)
from d100.wcf.wcf import wcf
from d100.wcf.utils import eight_versions


# Test entire wcf flow
def test_wcf():
    W, L, R = range(3)
    tiles = [
        [
            [W, W],
            [W, L],
        ],
    ]

    patterns = []
    for tile in tiles:
        patterns += eight_versions(tile)

    # N = 2
    wcf(patterns, 16)
