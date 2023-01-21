from random import *
class moves:
    def __init__(self, name, damage, type):
        self.name = name
        self.damage = damage
        self.type = type

class race:
    def __init__(self, race):
        self.race = race
        match race:
            case "undead":
                self.weakness = ["magic"]
                self.strength = ["poison"]
            case "human":
                self.weakness = ["fire"]
                self.strength = ["physical"]
            case "dwarf":
                self.weakness = ["poison"]
                self.strength = ["fire"]
            

class character:
    def __init__(self, name, maxHealth, health, move, armour, armourtype, dodge, critical,inventory, race, level, xp, gold, hiddenstr):
        self.name = name
        self.maxHealth = maxHealth
        self.health = health
        self.move = move
        self.armour = armour
        self.armourtype = armourtype
        self.dodge = dodge
        self.critical = critical
        self.inventory = inventory
        self.race = race
        self.level = level
        self.xp = xp
        self.gold = gold
        self.hiddenstr = hiddenstr
        
    def randomEnemy(amount):
        enemies = []
        x = randint(0, 100)
        #print(x)
        if x > 20:
            for y in range(amount):
                enemy = character(f"{y} Skeleton", 100, 100, moves("Slash", 10, "Physical"), 0, 0, 1,1,[],race("undead"), 0, 500, 10, "Enemy")
                enemies.append(enemy)
        else:
            for y in range(amount):
                enemy = character(f'{y} Cultist', 80, 80, moves("Slash",15,"Physical"), 0, 0, 5, 5, [], race("human"), 0, 700, 50, "Enemy")
                enemies.append(enemy)
        return enemies
        
level1 = 100
def levels(xp, level):
    global level1
    if xp >= level1:
        level += 1
        xp -= level1
        level1 = (level1)*1.5
        print("Now you need " + str(level1) + " xp to level up!")
        print("You leveled up!")
        print("You are now level " + str(level) + "!")
        levels(xp, level)
    return xp,level

def increaseStats(player):
    player.maxhealth += 5
    player
