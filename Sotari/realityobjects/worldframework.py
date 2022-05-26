from realityhandling.naming import regionname
from realityhandling.naming import continentname
import random

class World:
    def __init__(self, name, custom):
        self.name = name

        if not custom:
            self.continents = []
            regionsleft = 1000
            for i in range(random.randint(5, 11)):
                continentsize = random.randint(5, 50)
                while continentsize > regionsleft:
                    continentsize -= 1
                regionsleft -= continentsize
                self.continents.append(Continent(continentname(), continentsize))



class Continent:
    def __init__(self, name, size):
        self.name = name
        self.regions = []
        for i in range(size):
            self.regions.append(Region(regionname()))

class Island:
    def __init__(self, name):
        self.name = name
        self.region = Region(name)

class Region:
    def __init__(self, name):
        self.name = name

class Nation:
    def __init__(self, name):
        self.name = name