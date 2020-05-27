""" Class for the player """
from World import Location
import random


class Player():
    def __init__(self, name, location=None):
        self.name = name
        self.location = location

    def help(self):
        print('''Helpful commands:
        look
        use
        take
        talk
        go
        type help <command> for examples''')

    def move(self, place):
        if place in self.location.directions.keys():
            self.location = self.location.directions[place]
            print(f'{self.name} walked to the {place}')
        else:
            print("I can't move there right now")

    def look(self):
        print(self.location.description)


class RPGPlayer:
    def __init__(self, job):
        self.job = job
        self.hp = 10
        self.mp = 10
        self.strength = 10
        self.intelect = 10
        self.dexterity = 10
        self.weapon = None
        self.items = []

    def check_items(self):
        print('Held items:')
        for item in self.items:
            print(item)

    def combat(self, monster):
        press_attack = True
        while press_attack:
            print(f'player hp: {self.hp}\nmonster hp: {monster.hp}\n')
            action = input('choose an action:\nattack\nspell\nitem\nflee\n->')
            if action == 'attack':
                print('you choose to attack the monter')
                press_attack = self.attack(monster)
            elif action == 'spell':
                self.spell(monster)
            elif action == 'item':
                self.item()
            elif action == 'flee':
                self.flee()
            elif action == 'q':
                break
            else:
                print(f'{action} is not a valid command')

    def attack(self, monster):
        dmg_addition = random.randrange(0, 4)
        if self.weapon:
            if self.weapon.stat == 'str':
                ### Create a chance to hit thing
                damage = random.randrange(self.weapon.min_damage, self.weapon.max_damage +1)
                damage += (self.strength // 5)
                monster.hp -= damage
                print(f'You strike the monster with your {self.weapon.name} for {damage} damage')
            elif self.weapon.stat == 'dex':
                pass
            else:
                pass
        else:
            damage = 2 + (self.strength // 5)
            damage += dmg_addition
            monster.hp -= damage
            print(f'You struck the monster with your fists for {damage} damage')
        if monster.hp > 0:
            monster_damage = monster.give_damage()
            self.take_damage(monster_damage)
            print(f'The monster struck you for {monster_damage} damage')
            if self.hp > 0:
                return True
            else:
                print('The monster has felled you. Try again next time')
                return False
        else:
            print('you felled the monster, congratulations')
            return False

    def spell(self, monster):
        pass

    def item(self):
        pass

    def flee(self):
        pass

    def take_damage(self, damage):
        self.hp -= damage
        # Maybe put damage text here


class Warrior(RPGPlayer):
    def __init__(self):
        self.strength = 15
        self.intelect = 5
        self.dexterity = 10

class Rogue(RPGPlayer):
    def __init__(self):
        self.strength = 10
        self.intelect = 5
        self.dexterity = 15
