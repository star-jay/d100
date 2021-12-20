import random
import numpy as np


def random_points(n=250):
    return np.array(
        [
            [random.random(), random.random()]
            for x in range(n)
        ])


def random_color():
    return f"#{'%06x'%random.randint(0,16777215)}"
