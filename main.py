from hpdmg import *
from inv_shop import *
from item_descriptions import *
from character import *

            #name, health, move, armour, armourtype, dodge, critical, inventory, race, level, xp, gold, tag
mc = character("Doggo", 100 ,100, (moves("Punch", 50, "Physical"), moves("Kick", 15, "Physical"), moves("Slash", 15, "Physical")), 5, 0, 1, 1,[], race("human"), 0, 0, 0,"Player")
skeleton = character("Skeleton", 100, 100, moves("Slash", 10, "Physical"), 0, 0, 1, 1,[], race("undead"), 0, 500, 10, "Enemy")




inspectEnemy(skeleton)
inspectEnemy(mc)
#attack(mc, skeleton, mc.move[0])
while mc.health > 0 and skeleton.health > 0:
    if attack(mc, skeleton, mc.move[0]):
        break
    if attack(skeleton, mc, skeleton.move):
        break


print("End of battle!")