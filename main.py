from d100.wcf.wcf import wcf
from d100.wcf.utils import eight_versions


if __name__ == "__main__":
    W, L, R = range(3)
    W, L, R = ['≈', '.', '█']

    tiles = [
        [
            [W, W],
            [W, W],
        ],
        [
            [W, W],
            [W, L],
        ],
        [
            [W, L],
            [W, L],
        ],
        [
            [L, L],
            [L, L],
        ],
        [
            [R, L],
            [L, L],
        ],
        [
            [R, R],
            [L, L],
        ],
        [
            [R, R],
            [L, R],
        ],
    ]

    patterns = []
    for tile in tiles:
        patterns += eight_versions(tile)

    # N = 2
    bounds = 52

    wave = wcf(patterns, bounds)

    for y in range(bounds):
        print(''.join([
            ''.join(wave[y][x].tile[0])
            for x in range(bounds)
        ]))
        print(''.join([
            ''.join(wave[y][x].tile[1])
            for x in range(bounds)
        ]))
