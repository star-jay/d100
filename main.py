from d100.voronoi import voronoi, utils, draw
import random


random.seed(1)


class Region():
    """regions are polys in the world space"""
    def __init__(self, point, poly, region_index, neighbours):
        # self.poly = poly
        self.region_index = region_index
        self.point = point
        self.neighbours = neighbours
        self.poly = poly


class Kingdom():
    def generate(context):
        """generate a kingdom based on the context"""
        world = context.get('world', None)
        # create a region in that
        region = random.choice(world.regions)
        return Kingdom(starting_region=region)

    def __init__(self, starting_region):
        self.starting_region = starting_region
        self.color = utils.random_color()
        # take rule of region
        # if starting_region.kingdom is None:
        #     # starting_region.kingdom = self
        #     pass
        # else:
        #     # self.rebel()
        #     pass
        self.regions = [starting_region, ]

    def expand(self):
        """
        Pick a random neighbour and expand to it
        """
        for region in self.regions:
            neighbour = random.choice(region.neighbours)
            self.regions.append(neighbour)


class World():
    """A worls has regions"""

    def generate_worldmap(self):
        points = utils.random_points(200)
        vor = voronoi.voronoi_bounded(points, voronoi.bounding_box)
        points = vor.vertices

        points = voronoi.relax_points(points, n=1)

        # vor = voronoi(points)
        # points = vor.vertices
        self.vor = voronoi.voronoi_bounded(points, voronoi.bounding_box)
        self.regions = [
            Region(**region)
            for index, region
            in voronoi.region_ridge_and_neighbour(vor).items()
        ]

    def generate_kingdoms(self, n=7):
        # number of starting kingdoms:
        context = dict(world=self)
        self.kingdoms = [
            Kingdom.generate(context)
            for x in range(n)
        ]

    def debug(self):
        """gives some debug information"""
        # WIDTH, HEIGHT = 1000, 1000
        # SCALE = 1000
        # voronoi.plot_vornoi_diagram(self.vor, voronoi.bounding_box)
        # draw.draw_map(self.vor, WIDTH, HEIGHT, SCALE)
        draw.draw_world(self)

    def __init__(self):
        self.generate_worldmap()
        self.generate_kingdoms()

        for x in range(5):
            for kingdom in self.kingdoms:
                kingdom.expand()

        self.debug()


if __name__ == '__main__':
    World()

    # TODO:
    # define borders
    # expand regions
    # contest regions
