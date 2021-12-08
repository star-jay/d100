# utils for rotating creating the input
def switch_rows(matrix):
    return [
        [
            value
            for x, value in enumerate(row)
        ]
        for y, row in enumerate(matrix[::-1])
    ]


def switch_cols(matrix):
    return [
        row[-1::-1]
        for y, row in enumerate(matrix)
    ]


def rows_to_cols(matrix):
    return [
        [
            matrix[x][y]
            for x, value in enumerate(row)
        ]
        for y, row in enumerate(matrix)
    ]


def eight_versions(magic):
    # 1
    squares = [magic, ]
    # 2
    squares.extend([
        switch_rows(square)
        for square in squares
    ])
    # 4
    squares.extend([
        switch_cols(square)
        for square in squares
    ])
    # 8
    squares.extend([
        rows_to_cols(square)
        for square in squares
    ])
    return squares
