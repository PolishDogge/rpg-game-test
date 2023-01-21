from random import randint
damageGiven = 0

class moves:
    def __init__(self, name, damage, type):
        self.name = name
        self.damage = damage
        self.type = type

class player:
    def __init__(self, name, health, move, armour, armourtype, dodge, critical,inventory):
        self.name = name
        self.health = health
        self.move = move
        self.armour = armour
        self.armourtype = armourtype
        self.dodge = dodge
        self.critical = critical
        self.inventory = inventory

class enemy:
    def __init__(self, name, health, move, armour,armourtype, dodge, critical):
        self.name = name
        self.health = health
        self.move = move
        self.armour = armour
        self.armourtype = armourtype
        self.dodge = dodge
        self.critical = critical

#armor types
#0 = none 0%
#1 = light 15%
#2 = medium 25%
#3 = heavy 35%
#4 = v. heavy 55%
def checkarmour(armourtype, armour):
    match armourtype:
        case 0:
            return 0
        case 1:
            armour = (armour*5)/100
            if armour > 0.15:
                armour = 0.15
        case 2:
            armour = (armour*10)/100
            if armour > 0.25:
                armour = 0.25
        case 3:
            armour = (armour*15)/100
            if armour > 0.35:
                armour = 0.35
        case 4:
            armour = (armour*20)/100
            if armour > 0.55:
                armour = 0.55
    return armour

def attack(attacker, defender, move):
    global damageGiven
    damageGiven = 0
    
    if defender.dodge > randint(0, 100):
        print(defender.name + " dodged the attack!")
        return False
    else:
        if attacker.critical > randint(0, 100):
            print('Critical hit!')
            damageGiven = (move.damage* 2) - (move.damage*checkarmour(defender.armourtype,defender.armour))
        else:
            damageGiven = (move.damage - (move.damage*checkarmour(defender.armourtype,defender.armour)))
            
        
        if damageGiven < 0:
            damageGiven = 1
        defender.health -= damageGiven
        print(attacker.name + " attacked " + defender.name + " for " + str(damageGiven) + " damage!")
        
        if defender.health <= 0:
            print(defender.name + " died!")
            return True
        else:
            return False

def inspectEnemy(enemy):
    print(enemy.name + " has " + str(enemy.health) + " health left!")
    print(enemy.name + " has " + str(enemy.armour) + " armour, and has an armor type of " + str(enemy.armourtype) + ".")
    print(enemy.name + " has " + str(enemy.dodge) + " dodge.")
    print(enemy.name + " has " + str(enemy.critical) + " critical chance.")