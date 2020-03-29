""" Class for the player """
from World import Location


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
