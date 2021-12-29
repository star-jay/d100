import tkinter as tk
from .utils import random_color

WIDTH, HEIGHT = 1000, 1000
SCALE = 1000


def _scale_and_flip(point, scale, height, offset):
    """
    scales the provided point and flips the y axis so it points upwards
    origin (0, 0) at the bottom left corner of the screen
    returns the point scaled and flipped
    """
    print(point)
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

    for region in world.regions:
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

    root.mainloop()
