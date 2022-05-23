class Item:
    def __init__(self, name, value = 0, visibility = 0, mass = 0, size = 0):
        self.name = name
        self.value = value
        self.visibility = visibility
        self.mass = mass

    def set_value(self, new_value):
        self.value = new_value

    def set_name(self, new_name):
        self.name = new_name


class Equipment(Item):
    sus = 0
    threat = 0

    def set_suspicious(self, sus):
        self.sus = sus
    

class Weapon(Equipment):
    pass

class Armor(Equipment):
    pass

class Currency(Item):
    pass