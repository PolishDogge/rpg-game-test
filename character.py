from random import *
from character import *
from item_descriptions import *

class moves:
    def __init__(self, name, damage, type, type2, times):
        self.name = name
        self.damage = damage
        self.type = type
        self.type2 = type2
        self.times = times
        
#predefined moves
#[Todo] add more moves
punch = moves("Punch", 10, "Physical",None,1)
kick = moves("Kick", 15, "Physical", None,1)

slash = moves("Slash", 10, "Physical", None,1)
shieldbash = moves("Shield Bash", 15, "Physical", None,1)
quickslash = moves("Quick Slash", 5, "Physical", None,3)

poisonPotion = moves("Poison Potion", 10, "Poison", None,1)
posionDagger = moves("Poison Dagger", 15, "Poison", "Physical",1)

fireBall = moves("Fireball", 10, "Fire", "Magic",1)
thunderBolt = moves("Thunderbolt", 10, "Electric", "Magic",1)
iceSpike = moves("Ice Spike", 10, "Ice", "Magic",1)

bowUse = moves("Bow Use", 10, "Physical", "Ranged",1)
quickslashArcher = moves("Quick Slash", 5, "Physical", None,3)


class race:
    def __init__(self, race):
        self.race = race
        match race:
            #[Todo] change this to be more balanced
            #add boosts?
            case "undead":
                self.weakness = ["magic"]
                self.strength = ["poison"]
            case "demon":
                self.weakness = ["ice"]
                self.strength = ["fire"]
            case "angel":
                self.weakness = ["fire","electric"]
                self.strength = ["physical"]
            case "dragon":
                self.weakness = ["ice"]
                self.strength = ["fire","physical"]
            case "human":
                self.weakness = ["fire"]
                self.strength = ["physical"]
            case "dwarf":
                self.weakness = ["poison"]
                self.strength = ["fire"]
            case "elf":
                self.weakness = ["physical"]
                self.strength = ["electric"]
            case "orc":
                self.weakness = ["electric"]
                self.strength = ["ice"]
        match race:
            case 'human':
                self.hiddenBoost = ['physical']
            case 'dwarf':
                self.hiddenBoost = ['physical']
            case 'elf':
                self.hiddenBoost = ['archery']
            case 'orc':
                self.hiddenBoost = ['physical', 'dodge']

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
        print(f'{x} was generated in randomEnemy')
        if x > 20 and x < 40:
            for y in range(amount):
                enemy = character(f"{y} Skeleton", 100, 100, (slash), 0, 0, 1,1,[],race("undead"), 0, 500, 10, "Enemy")
                enemies.append(enemy)
        
        elif x > 40 and x < 60:
            for y in range(amount):
                enemy = character(f'{y} Cultist', 80, 80, (slash), 0, 0, 5, 5, [], race("human"), 0, 700, 50, "Enemy")
                enemies.append(enemy)
        
        elif x > 60 < 95:
            for y in range(amount):
                enemy = character(f'{y} Orc', 120, 120, (slash), 0, 0, 1, 1, [],race("orc"), 0, 1000, 100, "Enemy")
                enemies.append(enemy)
                
        elif x > 95 < 100:
            enemies.append(character("Dragon", 350, 350, (slash, fireBall), 0, 0, 1, 1, [], race("dragon"), 0, 2000, 500, "Enemy"))
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
    player.maxhealth += (player.maxhealth*0.1)
    player.health += 5
    player.dodge += 0.1
    player.critical += 0.1
    print("Your stats have increased!")
    print("Your max health is now " + str(player.maxhealth))
    

def createCharacter():
    name = input("What is your name? ").upper()
    print("Currently there are 4 classes: Warrior, Mage, Rogue and Archer")
    whatClass = input("What class do you want to be? ").lower()
    print('----------------------------------')
    print("Currently there are 4 races: Human, Dwarf, Elf, and Orc")
    whatRace = input("What race do you want to be? ").lower()
    
    match whatClass:
        case "warrior":
            player = character(name, 100, 100, (slash, punch, kick), 0, 0, 1,1,[wooden_sword, potion],race(str(whatRace)), 0, 0, 0, "Player")
        case "mage":
            player = character(name, 80, 80, (fireBall, thunderBolt),0,0,1,1,[staff,potion], race(str(whatRace)), 0, 0, 0, "Player")
        case "rogue":
            player = character(name, 90, 90, (quickslash,posionDagger),0,0,5,5,[dagger,potion], race(str(whatRace)), 0, 0, 0, "Player")
        case "archer":
            player = character(name, 90, 90, (quickslash, bowUse),0,0,5,5,[bow,dagger,potion], race(str(whatRace)), 0, 0, 0, "Player")
    return player