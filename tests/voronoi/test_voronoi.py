from d100.voronoi import voronoi, utils


def test_region_ridge_and_neighbour():
    points = utils.random_points(10)
    vor = voronoi.voronoi(points)
    assert voronoi.region_ridge_and_neighbour(vor)
