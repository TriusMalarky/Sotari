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

    defense = {
        "sharp": 0,
        "blunt": 0,
        "fire": 0,
        "ice": 0,
        "lightning": 0,
        "toxic": 0,
        "arcane": 0,
        "pure": 0
    }

    protection =  {
        "sharp": 0,
        "blunt": 0,
        "fire": 0,
        "ice": 0,
        "lightning": 0,
        "toxic": 0,
        "arcane": 0,
        "pure": 0
    }

    def set_suspicious(self, sus):
        self.sus = sus

    def set_threat(self, threat):
        self.threat = threat

    def set_protection(self, prot, amount):
        self.protection[prot] = amount

    def set_defense(self, defe, amount):
        self.defense[defe] = amount

class Weapon(Equipment):
    pass

class Armor(Equipment):
    pass

class Currency(Item):
    pass