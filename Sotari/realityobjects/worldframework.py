class World:
    def __init__(self, name):
        self.name = name


class Continent:
    def __init__(self, name):
        self.name = name

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