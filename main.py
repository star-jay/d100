from d100.voronoi import voronoi, utils, draw
import random


if __name__ == '__main__':
    WIDTH, HEIGHT = 500, 500
    SCALE = 500

    random.seed(1)

    points = utils.random_points(250)
    vor = voronoi.voronoi_bounded(points, voronoi.bounding_box)
    points = vor.vertices

    points = voronoi.relax_points(points)

    # vor = voronoi(points)
    # points = vor.vertices
    vor = voronoi.voronoi_bounded(points, voronoi.bounding_box)
    # min_max(points)
    # min_max(vor.vertices)

    # DEBUG
    voronoi.plot_vornoi_diagram(vor, voronoi.bounding_box)
    draw.draw_map(vor, WIDTH, HEIGHT, SCALE)
