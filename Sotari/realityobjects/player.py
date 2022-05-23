class Player:
    name = "New Player"

    sus = 0
    threat = 0

    hp = 0



    stats = {
        'physical': 0,
        'strength': 0,
        'endurance': 0,
        'agility': 0,

        'magical': 0,
        'energy': 0,
        'purity': 0,
        'manipulation': 0,

        'intellectual': 0,
        'technological': 0,
        'mechanical': 0,
        'material': 0,
    }


    def set_name(self, name):
        self.name = name

    def set_stat(self, stat, amount):
        self.stats[stat] = amount

    def increment_stat(self, stat):
        self.stats[stat] += 1

    def get_stat(self, stat):
        return self.stats[stat]