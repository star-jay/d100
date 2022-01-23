from d100.voronoi import voronoi, utils
import numpy as np


def test_region_ridge_and_neighbour():
    points = utils.random_points(10)
    # works only ony voronoi bounded
    bounding_box = np.array([0., 1., 0., 1.])
    vor = voronoi.voronoi_bounded(points, bounding_box)
    assert voronoi.region_ridge_and_neighbour(vor)
