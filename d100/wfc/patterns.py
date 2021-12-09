

def generate_tileset(example, n):
    """
        example: double sided array
        n: a signle tile has NxN dimensions
        bounds:
    """
    tileset = []
    for y in range(len(example)-n):
        for x in range(len(example[0])-n):

            tile = [
                [
                    example[yy][xx]
                    for xx in range(x, x+n)
                ]
                for yy in range(y, y+n)
            ]
            tileset.append(tile)
    return tileset
