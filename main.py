from d100.wfc.wfc import wfc
from d100.wfc.utils import eight_versions
from d100.wfc.patterns import generate_tileset


if __name__ == "__main__":
    W, L, R = range(3)
    W, L, R = ['≈', ' ', '█']

    tileset_1 = [
        [
            [W, W],
            [W, R],
        ],
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
            [W, L],
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

    tileset_2 = [
        [
            [L, R, L],
            [R, R, L],
            [L, L, L],
        ],
        [
            [L, R, L],
            [R, R, R],
            [L, R, L],
        ],
        [
            [R, R, L],
            [R, R, R],
            [L, R, L],
        ],
    ]

    example = """
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈
    ≈≈≈≈≈≈≈≈≈   ≈≈≈≈≈≈
    ≈≈≈  ≈≈≈     ≈≈≈≈≈
    ≈≈≈          ≈≈≈≈≈
    ≈≈≈     ██  ≈≈≈≈≈≈
    ≈≈≈≈≈   ███    ≈≈≈
    ≈≈≈≈≈≈  █     ≈≈≈≈
    ≈≈≈≈≈≈        ≈≈≈≈
    ≈≈≈≈≈≈≈≈    ≈   ≈≈
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
    tileset_3 = generate_tileset(example, N)

    for tile in tileset_3:
        for line in tile:
            print(line)

    patterns = []
    for tile in tileset_3:
        patterns += eight_versions(tile)

    # N = 2
    bounds = 3

    wave = wfc(patterns, bounds)

    for y in range(bounds):
        print(''.join([
            ''.join(wave[y][x].tile[0])
            for x in range(bounds)
        ]))
        print(''.join([
            ''.join(wave[y][x].tile[1])
            for x in range(bounds)
        ]))
