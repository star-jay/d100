from d100.wcf.constants import (UP, DOWN, RIGHT, LEFT)
from d100.wcf.wcf import Node
import pytest


def test_remove_invalid_options():
    patterns = [
        [
            [0, 0],
            [0, 0],
        ],
        [
            [1, 0],
            [0, 1],
        ],
    ]

    tiles = [
        [
            [1, 1],
            [0, 0],
        ],
    ]

    node = Node(0, 1, patterns)
    node.remove_invalid_options(tiles, direction=DOWN)
    assert len(node.options) == 1

    # incomming is not valid
    with pytest.raises(RuntimeError):
        node = Node(0, 0, patterns)
        node.remove_invalid_options(tiles, direction=UP)

    # Not valid
    with pytest.raises(RuntimeError):
        node = Node(0, 0, patterns)
        node.remove_invalid_options(tiles=[patterns[1], ], direction=UP)
    with pytest.raises(RuntimeError):
        node = Node(0, 0, patterns)
        node.remove_invalid_options(tiles=[patterns[1], ], direction=LEFT)
    with pytest.raises(RuntimeError):
        node = Node(0, 0, patterns)
        node.remove_invalid_options(tiles=[patterns[1], ], direction=RIGHT)
