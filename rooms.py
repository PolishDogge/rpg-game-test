from random import randint
from character import *
class room:
    def __init__(self, name, description, north, south, east, west, down, enemies,shop):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.enemies = enemies
        self.shop = shop
    
    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]
    
    def currentRoom(self, name, direction):
        self.name = name
        self.direction = direction
        



def roomGeneration(amount):
    global currentRoom
    amount = int(amount)
    print('Gnerating ' + str(amount) + ' rooms')
    for i in range(amount):
        randomEnemies = []
        for b in range(randint(1, 3)):
            randomEnemies.append(character.randomEnemy(1)) 
        
        print('Room ' + str(i) + ' generated')
        globals()["room" + str(i)] = room("room" + str(i), "room" + str(i), None, None, None, None, None, randomEnemies, False)
    
    #12| 13| 14| 15
    #8 | 9 | 10| 11
    #4 | 5 | 6 | 7
    #0 | 1 | 2 | 3
    
    #automatically generate the room connections
    for i in range(amount):
        if i % 4 != 0:
            globals()["room" + str(i)].west = "room" + str(i - 1)
            globals()["room" + str(i - 1)].east = "room" + str(i)
        if i > 3:
            globals()["room" + str(i)].south = "room" + str(i - 4)
            globals()["room" + str(i - 4)].north = "room" + str(i)
    
    #randomly generate a shop
    for shopAmount in range(1, int(amount - (amount * 0.75))):
        shopRoom = randint(0, int(amount - 1))
        print("Shop generated in room " + str(shopRoom))
        globals()["room" + str(shopRoom)].shop = True
        
    #Debugging room/path generation
    for i in range(amount):
        print(globals()["room" + str(i)].name + ":")
        print(globals()["room" + str(i)].north)
        print(globals()["room" + str(i)].south)
        print(globals()["room" + str(i)].east)
        print(globals()["room" + str(i)].west)
        print("")


roomGeneration(16)
CurrentRoom = room0
def moveRoom(direction):
    global CurrentRoom
    if getattr(CurrentRoom, direction) != None:
        CurrentRoom = globals()[getattr(CurrentRoom, direction)]
    else:
        print("You can't go that way")
    
