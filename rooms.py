from random import randint
from character import *
from time import sleep
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
    
    def currentRoom(self, name, description):
        self.name = name
        self.direction = description
        

def roomGeneration(amount):
    global CurrentRoom
    amount = int(amount)
    print('Gnerating ' + str(amount) + ' rooms')
    for i in range(amount):
        randomEnemies = []
        #for b in range(randint(1, 3)):
        #    randomEnemies.append(character.randomEnemy(1)) 
        
        print('Room ' + str(i) + ' generated')
        globals()["room" + str(i)] = room("room" + str(i), "room" + str(i), None, None, None, None, None, randomEnemies, False)
    
    #12| 13| 14| 15
    #8 | 9 | 10| 11
    #4 | 5 | 6 | 7
    #0 | 1 | 2 | 3
    generatePaths(amount)
    generateShop(amount)
    return globals()["room" + str(0)]
    
    #automatically generate the room connections
def generatePaths(amount):
    for i in range(amount):
        if i % 4 != 0:
            globals()["room" + str(i)].west = "room" + str(i - 1)
            globals()["room" + str(i - 1)].east = "room" + str(i)
        if i > 3:
            globals()["room" + str(i)].south = "room" + str(i - 4)
            globals()["room" + str(i - 4)].north = "room" + str(i)
    
       #Debugging room/path generation
    for i in range(amount):
        print(globals()["room" + str(i)].name + ":")
        print(globals()["room" + str(i)].north)
        print(globals()["room" + str(i)].south)
        print(globals()["room" + str(i)].east)
        print(globals()["room" + str(i)].west)
        print("")
    
    #randomly generate a shop
def generateShop(amount):
    shopblacklist = []
    for shopAmount in range(1, int(amount - (amount * 0.75))):
        shopRoom = randint(0, int(amount - 1))
        if shopRoom in shopblacklist:
            print("Shop already generated in room " + str(shopRoom))
            continue
        print("Shop generated in room " + str(shopRoom))
        globals()["room" + str(shopRoom)].shop = True
        

    
#current room is room0
CurrentRoom = roomGeneration(16)
print("Current room: " + CurrentRoom.name)
print("To the north is: " + CurrentRoom.north)
#move to any room in the grid by typing the direction you want to move in
def move(direction):
    global CurrentRoom
    if direction == "north" and CurrentRoom.north == None:
        print("You can't move in that direction")
        return
    elif direction == "south" and CurrentRoom.south == None:
        print("You can't move in that direction")
        return
    elif direction == "east" and CurrentRoom.east == None:
        print("You can't move in that direction")
        return
    elif direction == "west" and CurrentRoom.west == None:
        print("You can't move in that direction")
        return
    else:
        CurrentRoom = globals()[CurrentRoom.__dict__[direction]]
        print("You are now in " + CurrentRoom.name)
        return CurrentRoom
    