from random import randint
class room:
    def __init__(self, name, description, north, south, east, west, down, enemies):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.enemies = enemies
    
    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]



#for i in range(16):
#    randomEnemies = []
#    for i in range(randint(0, 3)):
#        randomEnemies.append()
#        
#    globals()["room" + str(i)] = room("room" + str(i), "room" + str(i), None, None, None, None, None, randomEnemies)
        