"""

[ ] tiles
[ ] match tiles in direction

[ ] pick tile => neighbours will have less matches

"""
import random
from .constants import direction_offsets, UP, DOWN, LEFT, RIGHT


def get_neighbours(x, y, bounds):
    return {
        direction:
        (x + direction[0], y + direction[1])
        for direction in direction_offsets
        if all([
            x + direction[0] < bounds,
            x + direction[0] >= 0,
            y + direction[1] < bounds,
            y + direction[1] >= 0,
        ])
    }


def match_patterns(pattern, neighbour, direction):
    # up
    if direction == UP:
        return pattern[0] == neighbour[-1]

    if direction == DOWN:
        return pattern[-1] == neighbour[0]

    if direction == LEFT:
        return [row[0] for row in pattern] == [row[-1] for row in neighbour]

    if direction == RIGHT:
        return [row[-1] for row in pattern] == [row[0] for row in neighbour]


class Node():
    neighbours = dict()

    def __init__(self, x, y, patterns):
        # know your relative position
        self.x = x
        self.y = y

        # Starting options are all patterns
        self.options = patterns

    @property
    def tile(self):
        if len(self.options) == 1:
            return self.options[0]

    def remove_invalid_options(self, tiles, direction):
        # dont remove options if we have picked a tile
        if self.tile:
            return
        # based on direction eliminate own options
        old_options = len(self.options)
        self.options = [
            option
            for option in self.options
            if any([
                match_patterns(tile, option, direction)
                for tile in tiles
            ])
        ]
        if len(self.options) == 0:
            raise RuntimeError(f"No options available for {self.x, self.y}")

        if len(self.options) < old_options:
            self.propegate()

    def pick_option(self):
        if len(self.options) == 0:
            raise RuntimeError(f"No options available for {self.x, self.y}")

        # if we pick an option
        self.options = [self.options[random.randrange(0, len(self.options))]]
        # pass through neighbours
        self.propegate()

    def propegate(self):
        for direction, node in self.neighbours.items():
            node.remove_invalid_options(self.options, direction)


def find_node(nodes):
    pick_from = [node for node in nodes if not node.tile]
    if len(pick_from) == 0:
        return
    return min(pick_from, key=lambda x: len(x.options))


def wfc(patterns, bounds):
    wave = [
        [
            Node(x, y, patterns)
            for x in range(bounds)
        ]
        for y in range(bounds)
    ]

    all_nodes = [
        node
        for row in wave
        for node in row
    ]

    for node in all_nodes:
        node.wave = wave

        node.neighbours = {
            direction: wave[coordinates[1]][coordinates[0]]
            for direction, coordinates
            in get_neighbours(node.x, node.y, bounds).items()
        }

    solving = True
    while solving:
        solving = False
        node = find_node(all_nodes)
        if not node:
            break

        solving = True

        node.pick_option()

    return wave
