from random import randint
from character import *
from inv_shop import *
from item_descriptions import *
from HPdmg import *

def randomRoomName():
    randomName = ''
    for i in range(randint(1, 10)):
        randomName += chr(randint(65, 90))
    return randomName

class room:
    def __init__(self, name, description, north, south, east, west, down, enemies, shop, treasure):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.enemies = enemies
        self.shop = shop
        self.treasure = treasure
    
    def currentRoom(self, name, description):
        self.name = name
        self.direction = description
        

def roomGeneration(amount):
    global CurrentRoom
    amount = int(amount)
    print('Gnerating ' + str(amount) + ' rooms')
    for i in range(amount):
        randomEnemies = []
        for b in range(randint(1, 3)):
            randomEnemies.append(character.randomEnemy(1)) 
        
        print('Room ' + str(i) + ' generated')
        globals()["room" + str(i)] = room("room" + str(i), randomRoomName(), None, None, None, None, None, randomEnemies, False, False)
    
    #12| 13| 14| 15
    #8 | 9 | 10| 11
    #4 | 5 | 6 | 7
    #0 | 1 | 2 | 3
    generatePaths(amount)
    generateSpecial(amount)
    
    globals()["room0"].enemies = []
    
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
    #for i in range(amount):
    #    print(globals()["room" + str(i)].name + ":")
    #    print(globals()["room" + str(i)].north)
    #    print(globals()["room" + str(i)].south)
    #    print(globals()["room" + str(i)].east)
    #    print(globals()["room" + str(i)].west)
    #    print("")
    
    #randomly generate a shop
def generateSpecial(amount):
    shopblacklist = []
    for shopAmount in range(1, int(amount - (amount * 0.75))):
        shopRoom = randint(0, int(amount - 1))
        if shopRoom in shopblacklist:
            print("Shop already generated in room " + str(shopRoom))
            continue
        #print("Shop generated in room " + str(shopRoom))
        globals()["room" + str(shopRoom)].shop = True
        globals()["room" + str(shopRoom)].enemies = []
        globals()["room" + str(shopRoom)].description = "A shop"
        shopblacklist.append(shopRoom)
    for treasureAmount in range(1, round(int((amount*0.2)))):
        treasureRoom = randint(0, int(amount - 1))
        if treasureRoom in shopblacklist:
            print("Treasure already generated in room " + str(treasureRoom))
            continue
        #print("Treasure generated in room " + str(treasureRoom))
        globals()["room" + str(treasureRoom)].treasure = True
        shopblacklist.append(treasureRoom)

        

    
#current room is room0
CurrentRoom = roomGeneration(16)

print("Current room: " + CurrentRoom.name)
print("To the north is: " + CurrentRoom.north)
#move to any room in the grid by typing the direction you want to move in
def move(direction, player):
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
        checkRoom(globals()[CurrentRoom.name], player)
        return CurrentRoom
    
#print out all directions player can go
def directions():
    print("You can go:")
    if CurrentRoom.north != None:
        print("North to " + CurrentRoom.north)
    if CurrentRoom.south != None:
        print("South to " + CurrentRoom.south)
    if CurrentRoom.east != None:
        print("East to " + CurrentRoom.east)
    if CurrentRoom.west != None:
        print("West to " + CurrentRoom.west)
    print("")

def checkRoom(room, player):
    if room.enemies == []:
        print("There are no enemies in this room")
        if room.shop == True:
            print("There is a shop in this room")
            shop.shop(player)
        elif room.treasure == True:
            print("There is treasure in this room")
            treasureRoom(player, room)
    else:
        print("There are enemies in this room")
        fighting(player, room)
    print("")


def treasureRoom(room ,player):
    print("There is a chest in this room")
    print("Do you want to open it?")
    inp = input(">>> ")
    if inp == "yes" or "y" or "Yes" or "Y":
        print("You open the chest and find:")
        coinamount = randint(1, 1000)
        print(str(coinamount) + " coins")
        player.coins += coinamount
        print("You now have " + str(player.coins) + " coins")
    else:
        print("You leave the chest alone")
        room.treasure = False

def printOutRoomNames():
    for i in range(16):
        print(globals()["room" + str(i)].name + ":" + globals()["room" + str(i)].description)

roomGeneration(16)
printOutRoomNames()