import tkinter as tk
from d100.voronoi.utils import random_color
import numpy as np


WIDTH, HEIGHT = 1000, 1000
SCALE = 1000


def _scale_and_flip(point, scale, height, offset):
    """
    scales the provided point and flips the y axis so it points upwards
    origin (0, 0) at the bottom left corner of the screen
    returns the point scaled and flipped
    """
    x, y = point
    ox, oy = offset
    return ((x+ox) * scale, height - (y+oy) * scale)


def scale_and_flip(polygon, scale, height, offset=(0, 0)):
    """
    scales the provided point and flips the y axis so it points upwards
    origin (0, 0) at the bottom left corner of the screen
    returns a sequence of scaled and flipped points representing the polygon
    ready to render
    """
    return [_scale_and_flip(point, scale, height, offset) for point in polygon]


def draw_vor(vor, width, height, scale):
    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height, bg='cyan')
    canvas.pack()

    for region in vor.filtered_regions:
        if len(region) > 0:
            poly = [vor.vertices[point] for point in region]
            poly = scale_and_flip(poly, scale, height)
            canvas.create_polygon(
                poly,
                fill=random_color(), outline='black')

    root.mainloop()


def draw_world(world, width=WIDTH, height=HEIGHT, scale=SCALE):
    """regions is dict"""
    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height, bg='cyan')
    canvas.pack()

    for index, region in world.regions.items():
        poly = scale_and_flip(region.poly, scale, height)
        canvas.create_polygon(
            poly,
            fill='gray', outline='black'
        )

    for kingdom in world.kingdoms:
        for region in kingdom.regions:
            poly = region.poly

            poly = scale_and_flip(poly, scale, height)
            canvas.create_polygon(
                poly,
                fill=kingdom.color, outline='black'
            )

            poly = scale_and_flip(poly, scale, height)
            canvas.create_polygon(
                poly,
                fill=kingdom.color, outline='black'
            )

            for points, vertices in region.borders.items():
                poly = [world.vor.vertices[v] for v in vertices]

                poly = scale_and_flip(poly, scale, height)
                canvas.create_line(poly, fill='red',)

                neighbour_point = [point for point in points if point != region.index][0]
                neighbour_region = world.vor.point_region[neighbour_point]
                poly = [world.vor.vertices[v] for v in world.vor.regions[neighbour_region]]
                poly = scale_and_flip(poly, 1000, 1000)
                canvas.create_polygon(poly, fill='blue', outline='black')

    root.mainloop()
