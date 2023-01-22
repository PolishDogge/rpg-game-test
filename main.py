from HPdmg import *
from inv_shop import *
from item_descriptions import *
from character import *
from rooms import *

            #name, max health, health, move, armour, armourtype, dodge, critical, inventory, race, level, xp, gold, tag
skeleton = character("Skeleton", 100, 100, moves("Slash", 10, "Physical", None, 1), 0, 0, 1, 1,[], race("undead"), 0, 500, 10, "Enemy")
mc = createCharacter()


#name, description, north, south, east, west, down, enemies
for i in range(5):
    globals()["room"+ str(i)] = room("room"+ str(i), "room"+ str(i), None, None, None, None, None, character.randomEnemy(randint(0, 3)))

current_node = room0
directions = ['north', 'south', 'east', 'west', 'down']
short_directions = ['n', 's', 'e', 'w', 'd']
print('Room0 enemies: ')
for i in range(len(current_node.enemies)):
    print(current_node.enemies[i].name)

print("You are in " + current_node.name)

print('-' * 20)
print('Character stats:')
print('-' * 20)
print("Name: " + mc.name)
print("Health: " + str(mc.health) + "/" + str(mc.maxHealth))
for i in range(len(mc.move)):
    print("Move " + str(i+1) + ": " + mc.move[i].name)
print("Armour: " + str(mc.armour))
print("Armour type: " + str(mc.armourtype))
print("Dodge: " + str(mc.dodge))
print("Critical chance: " + str(mc.critical))
for i in range(len(mc.inventory)):
    print("Inventory " + str(i+1) + ": " + mc.inventory[i].name)
print('Current XP: ' + str(mc.xp))
print('Current level: ' + str(mc.level))
print('Current gold: ' + str(mc.gold))