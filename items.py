""" code for all the items in the rpg """

class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight


class Weapon(Item):
    def __init__(self, name, min_damage, max_damage,
                 stat, element=None):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.stat = stat
        self.element = element
