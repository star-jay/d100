
def print_min_max(points):
    minx = min([x for x, y in points])
    miny = min([y for x, y in points])

    maxy = max([x for x, y in points])
    maxx = max([y for x, y in points])

    print(minx, miny, maxx, maxy)
