import scipy as sp
import scipy.spatial

import numpy as np
import matplotlib.pyplot as pl
from lloyd import Field
import sys


bounding_box = np.array([0., 1., 0., 1.])  # [x_min, x_max, y_min, y_max]
eps = sys.float_info.epsilon


def relax_points(points, n=3):
    # create a lloyd model on which one can perform iterations
    field = Field(points)

    # run one iteration of Lloyd relaxation on the field of points
    for x in range(n):
        field.relax()
        field.relax()
        field.relax()

    return field.get_points()


def voronoi(points):
    return scipy.spatial.Voronoi(points)


def in_box(towers, bounding_box):
    return np.logical_and(np.logical_and(bounding_box[0] <= towers[:, 0],
                                         towers[:, 0] <= bounding_box[1]),
                          np.logical_and(bounding_box[2] <= towers[:, 1],
                                         towers[:, 1] <= bounding_box[3]))


def voronoi_bounded(towers, bounding_box):
    # Select towers inside the bounding box
    i = in_box(towers, bounding_box)
    # Mirror points
    points_center = towers[i, :]
    points_left = np.copy(points_center)
    points_left[:, 0] = bounding_box[0] - (points_left[:, 0] - bounding_box[0])
    points_right = np.copy(points_center)
    points_right[:, 0] = bounding_box[1] + (bounding_box[1] - points_right[:, 0])  # noqa
    points_down = np.copy(points_center)
    points_down[:, 1] = bounding_box[2] - (points_down[:, 1] - bounding_box[2])
    points_up = np.copy(points_center)
    points_up[:, 1] = bounding_box[3] + (bounding_box[3] - points_up[:, 1])
    points = np.append(points_center,
                       np.append(np.append(points_left,
                                           points_right,
                                           axis=0),
                                 np.append(points_down,
                                           points_up,
                                           axis=0),
                                 axis=0),
                       axis=0)
    # Compute Voronoi
    vor = sp.spatial.Voronoi(points)
    # Filter regions
    regions = []
    for region in vor.regions:
        flag = True
        for index in region:
            if index == -1:
                flag = False
                break
            else:
                x = vor.vertices[index, 0]
                y = vor.vertices[index, 1]
                if not(bounding_box[0] - eps <= x and x <= bounding_box[1] + eps and  # noqa
                       bounding_box[2] - eps <= y and y <= bounding_box[3] + eps):  # noqa
                    flag = False
                    break
        if region != [] and flag:
            regions.append(region)
    vor.filtered_points = points_center
    vor.filtered_regions = regions
    return vor


# Plot it:
def plot_voronoi(voronoi):
    scipy.voronoi_plot_2d(voronoi)
    pl.show()


def plot_vornoi_diagram(vor, bounding_box, show_figure=True):
    # Initializes pyplot stuff
    fig = pl.figure()
    ax = fig.gca()

    # Plot initial points
    ax.plot(vor.filtered_points[:, 0], vor.filtered_points[:, 1], 'b.')

    # Plot ridges points
    for region in vor.filtered_regions:
        vertices = vor.vertices[region, :]
        ax.plot(vertices[:, 0], vertices[:, 1], 'go')

    # Plot ridges
    for region in vor.filtered_regions:
        vertices = vor.vertices[region + [region[0]], :]
        ax.plot(vertices[:, 0], vertices[:, 1], 'k-')

    # stores references to numbers for setting axes limits
    margin_percent = .1
    width = bounding_box[1]-bounding_box[0]
    height = bounding_box[3]-bounding_box[2]

    ax.set_xlim([bounding_box[0]-width*margin_percent, bounding_box[1]+width*margin_percent])  # noqa
    ax.set_ylim([bounding_box[2]-height*margin_percent, bounding_box[3]+height*margin_percent])  # noqa

    if show_figure:
        pl.show()
    return fig


def centroid_region(vertices):
    # Polygon's signed area
    A = 0
    # Centroid's x
    C_x = 0
    # Centroid's y
    C_y = 0
    for i in range(0, len(vertices) - 1):
        s = (vertices[i, 0] * vertices[i + 1, 1] - vertices[i + 1, 0] * vertices[i, 1])  # noqa
        A = A + s
        C_x = C_x + (vertices[i, 0] + vertices[i + 1, 0]) * s
        C_y = C_y + (vertices[i, 1] + vertices[i + 1, 1]) * s
    A = 0.5 * A
    C_x = (1.0 / (6.0 * A)) * C_x
    C_y = (1.0 / (6.0 * A)) * C_y
    return np.array([[C_x, C_y]])


def region_ridge_and_neighbour(vor):
    results = {}

    for index, point in enumerate(vor.filtered_points):
        region_index = vor.point_region[index]
        region = vor.regions[region_index]
        poly = vor.vertices[region, :]
        # poly = [vor.vertices[v] for v in vor.regions[region_index]],

        results[index] = dict(
            point=point,
            region_index=region_index,
            poly=poly,
            neighbours={
                [k for k in key if k != region_index][0]: border
                for key, border in vor.ridge_dict.items()
                if region_index in key and -1 not in key
                if -1 not in border
            }
        )

    return results
