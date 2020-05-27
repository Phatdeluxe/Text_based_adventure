'''Sample for turn based combat'''

from Player import Player, RPGPlayer
from monster import Monster
from items import Item, Weapon

monster = Monster(name='imp', hp=10, attack_min=3, attack_max=5,
                  armor=0, speed=0)

axe = Weapon(name='axe', min_damage=2,
             max_damage=5, stat='str')

player = RPGPlayer('warrior')

player.weapon = axe

player.combat(monster)

print('combat finished')
