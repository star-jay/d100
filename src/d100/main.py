from d100.voronoi import voronoi, utils, draw
import random


random.seed(1)


class Region():
    """regions are polys in the world space"""
    def __init__(self, world, index, point, poly, region_index, borders):

        self.world = world

        self.index = index
        self.point = point
        self.region_index = region_index
        self.poly = poly
        self.borders = borders

    def invade(self, kingdom):
        # if not resisting:
        self.kingdom = kingdom


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

    def expand(self):
        """
        Pick a random neighbour and expand to it
        """
        for region in self.regions:
            border = random.choice(region.borders)
            self.world.invade(self, border)


class World():
    """A worls has regions"""

    def __init__(self):
        self.generate_worldmap(n=250)
        self.generate_kingdoms(n=5)

        # for x in range(5):
        #     for kingdom in self.kingdoms:
        #         kingdom.expand()

        # self.debug()

    def generate_worldmap(self, n=200):
        points = utils.random_points(n)
        vor = voronoi.voronoi_bounded(points, voronoi.bounding_box)
        points = vor.vertices

        points = voronoi.relax_points(points, n=1)

        # 1 Ddevide the map in voronoi regions
        # Create bounded vornoi, all regions are inside the bounding box
        vor = voronoi.voronoi_bounded(points, voronoi.bounding_box)
        self.vor = vor

        graph = voronoi.region_ridge_and_neighbour(vor)

        self.regions = {
            index: Region(world=self, **region)
            for index, region in graph.items()
        }

    def create_biomes(self):
        # create a noise map
        # set height of region based on height map
        pass

    def create_rivers(self):
        # run river from source to sea
        # run
        pass

    def generate_kingdoms(self, n=7):
        # number of starting kingdoms:
        context = dict(world=self)
        self.kingdoms = [
            Kingdom.generate(context)
            for x in range(n)
        ]

    def debug(self):
        """gives some debug information"""
        draw.draw_world(self)


if __name__ == '__main__':
    World()

    # TODO:
    # define borders
    # expand regions
    # contest regions
