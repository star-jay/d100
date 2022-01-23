from d100.wfc.wfc import match_patterns
from d100.wfc.constants import UP, DOWN, RIGHT, LEFT


def test_simple_pattern():
    pattern = [[0]]
    neighbour = [[0]]
    direction = UP

    assert match_patterns(pattern, neighbour, direction)


def test_simple_pattern_true():
    pattern = [[0]]
    neighbour = [[1]]
    direction = UP

    assert not match_patterns(pattern, neighbour, direction)


def test_patters_up():
    pattern = [
        [0, 0],
        [0, 0],
    ]
    neighbour = [
        [1, 1],
        [0, 0],
    ]

    direction = UP
    assert match_patterns(pattern, neighbour, direction)
    direction = DOWN
    assert not match_patterns(pattern, neighbour, direction)


def test_patters_down():
    pattern = [
        [0, 0],
        [0, 0],
    ]
    neighbour = [
        [0, 0],
        [1, 1],
    ]

    direction = DOWN
    assert match_patterns(pattern, neighbour, direction)
    direction = UP
    assert not match_patterns(pattern, neighbour, direction)


def test_patters_left():
    pattern = [
        [0, 0],
        [0, 0],
    ]
    neighbour = [
        [1, 0],
        [1, 0],
    ]

    direction = LEFT
    assert match_patterns(pattern, neighbour, direction)
    direction = RIGHT
    assert not match_patterns(pattern, neighbour, direction)


def test_patters_right():
    pattern = [
        [0, 0],
        [0, 0],
    ]
    neighbour = [
        [0, 1],
        [0, 1],
    ]

    direction = RIGHT
    assert match_patterns(pattern, neighbour, direction)
    direction = LEFT
    assert not match_patterns(pattern, neighbour, direction)
    direction = UP
    assert not match_patterns(pattern, neighbour, direction)


def test_patters_false():
    pattern = [
        [0, 0],
        [0, 0],
    ]
    neighbour = [
        [1, 1],
        [1, 1],
    ]

    direction = RIGHT
    assert not match_patterns(pattern, neighbour, direction)
    direction = LEFT
    assert not match_patterns(pattern, neighbour, direction)
    direction = UP
    assert not match_patterns(pattern, neighbour, direction)
    direction = DOWN
    assert not match_patterns(pattern, neighbour, direction)
