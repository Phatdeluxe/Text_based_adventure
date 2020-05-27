''' Code for monsters'''
import random

class Monster:
    def __init__(self, name, hp, attack_min,
                 attack_max, armor, speed):
        self.name = name
        self.hp = hp
        self.attack_min = attack_min
        self.attack_max = attack_max
        self.armor = armor
        self.speed = speed

    def give_damage(self):
        damage = random.randrange(self.attack_min, self.attack_max + 1)
        return damage
