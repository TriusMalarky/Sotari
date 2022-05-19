class Item:
    def __init__(self, name, value = 0):
        self.name = name
        self.value = value


class Equipment(Item):
    pass


class Weapon(Equipment):
    pass

class Currency(Item):
    pass