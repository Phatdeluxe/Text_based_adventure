""" classes for locations """

# I would like to add cardinal directions to allow
# the player to move between loactions
# but also allow players to move around each location

class Location():
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.directions = {}
        self.pois = []

class Point_of_interest(Location):
    def __init__(self):
        super().__init__()


class Room:
    def __init__(self, name):
        self.name = name

class MonsterRoom(Room):
    def __init__(self, monster):
        self.monster = monster
