""" new text for the adventure """

from Player import Player
from World import Location

tutorial = Location('tutorial area')
tutorial.description = 'A sparsely populated area with only a tree and an old man sitting beneath it.'


foyer = Location('foyer')
foyer.description = 'A well lit foyer with stairs leading up and down, and doors to both the left and right.'

study = Location('study')
study.description = 'A dimly lit room with lots of books and maps. Smoke from a recently extinguished cigar fills the air. There is a door back into the foyer'

kitchen = Location('kitchen')
kitchen.description = 'A small table sits in the center of the room. The sound of dripping water is emenating from the sink. There are doors into the dining room and the foyer'

diningroom = Location('Dining room')
diningroom.description = 'A nicely set table take up the majority of this room. A caibnet full of silverware and plates sit at one end of the room. There are doors back into the kitchen and into the hallway'

hallway = Location('Hallway')
hallway.description = 'A small hallway that leads to a mud room. There are doors to the dining room, the mudroom and a closet'

closet = Point_of_interest('closet')
closet.description =


tutorial.directions['foyer'] = foyer

foyer.directions['study'] = study
foyer.directions['kitchen'] = kitchen

study.directions['foyer'] = foyer

kitchen.directions['foyer'] = foyer
kitchen.directions['dining room'] = diningroom


cmd = input('Please enter a name:')

player = Player(name=cmd, location=tutorial)

while True:
    cmd = input('->')

    if cmd == 'q':
        break
    if cmd[:2] == 'go':
        player.move(cmd[3:])
    elif cmd[:4] == "look":
        player.look()
