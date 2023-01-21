from HPdmg import *
from inv_shop import *
from item_descriptions import *
from character import *
from rooms import *

            #name, max health, health, move, armour, armourtype, dodge, critical, inventory, race, level, xp, gold, tag
mc = character("Doggo", 100 ,80, (moves("Punch", 50, "Physical"), moves("Kick", 15, "Physical"), moves("Slash", 15, "Physical")), 5, 0, 1, 1,[], race("human"), 0, 0, 0,"Player")
skeleton = character("Skeleton", 100, 100, moves("Slash", 10, "Physical"), 0, 0, 1, 1,[], race("undead"), 0, 500, 10, "Enemy")

room0 = None
room1 = None
room2 = None
room3 = None
room4 = None
room5 = None

for i in range(5):
    globals()["room"+ str(i)] = room("room"+ str(i), "room"+ str(i), None, None, None, None, None, character.randomEnemy(randint(0, 3)))

current_node = room0
directions = ['north', 'south', 'east', 'west', 'down']
short_directions = ['n', 's', 'e', 'w', 'd']
print(room0.enemies[0].name)