# from wfc.constants import (UP, DOWN, RIGHT, LEFT)
# from wfc.wfc import wfc
# from wfc.utils import eight_versions
from wfc.patterns import generate_tileset


# Test entire wfc flow
def test_wfc_3():

    # W, L, R = ['≈', ' ', '█']

    example = """
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈LLL≈≈≈≈≈≈
    ≈≈≈LL≈≈≈LLLLL≈≈≈≈≈
    ≈≈≈LLLLLLLLLL≈≈≈≈≈
    ≈≈≈LLLLLRRLL≈≈≈≈≈≈
    ≈≈≈≈≈LLLRRRLLLL≈≈≈
    ≈≈≈≈≈≈LLRLLLLL≈≈≈≈
    ≈≈≈≈≈≈LLLLLLLL≈≈≈≈
    ≈≈≈≈≈≈≈≈LLLL≈LLL≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    """
    example = example.lstrip().rstrip()
    example = example.splitlines()
    example = [
        line.lstrip().rstrip()
        for line in example
    ]

    N = 3
    tiles = generate_tileset(example, N)
    assert len(tiles) == (len(example)-N)*(len(example[0])-N)

    for tile in tiles:
        assert len(tile) == N
        for n in range(N):
            assert len(tile[n]) == N
