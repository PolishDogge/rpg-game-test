from random import randint
from character import levels

damageGiven = 0

#armor types
#0 = none 5%
#1 = light 15%
#2 = medium 25%
#3 = heavy 35%
#4 = v. heavy 55%
def checkarmour(armourtype, armour):
    match armourtype:
        case 0:
            armour = (armour)/100 
            if armour > 0.05:
                armour = 0.05
        case 1:
            armour = (armour)/100
            if armour > 0.15:
                armour = 0.15
        case 2:
            armour = (armour)/100
            if armour > 0.25:
                armour = 0.25
        case 3:
            armour = (armour*1.2)/100
            if armour > 0.35:
                armour = 0.35
        case 4:
            armour = (armour*1.45)/100
            if armour > 0.55:
                armour = 0.55
    return armour

def attack(attacker, defender, move):
    global damageGiven
    damageGiven = 0
    
    if move.type in defender.race.weakness:
        move.damage *= 2
        print("It's super effective!")
    elif move.type in defender.race.strength:
        move.damage /= 2
        print("It's not very effective...")
    
    if defender.dodge > randint(0, 100):
        print(defender.name + " dodged the attack!")
        return False
    else:
        for attacktimes in range(1, move.times):
            if attacker.critical > randint(0, 100):
                print('Critical hit!')
                damageGiven = (move.damage* 2) - (move.damage*checkarmour(defender.armourtype,defender.armour))
            else:
                damageGiven = (move.damage - (move.damage*checkarmour(defender.armourtype,defender.armour)))
        print(''+defender.name+' got attacked'+ str(attacktimes) + ' times!') 
        
        if damageGiven < 0:
            damageGiven = 1
        defender.health -= damageGiven
        print(attacker.name + " attacked " + defender.name + " for " + str(damageGiven) + " damage!")
        print(defender.name + " has " + str(defender.health) + " health left!")
        
        if defender.health <= 0:
            print(defender.name + " died!")
            if attacker.hiddenstr == "Player":
                if defender.xp > 0:
                    attacker.xp += (defender.xp)
                    print(attacker.name + " gained " + str(defender.xp) + " xp!")
                    attacker.xp, attacker.level = levels(attacker.xp, attacker.level)
                    attacker.gold += (defender.gold)
                    print(attacker.name + " gained " + str(defender.gold) + " gold!")
                    input("Press Enter to continue...")
                    print("--------------------")
            return True
        else:
            input("Press Enter to continue...")
            print("--------------------")
            return False
        

def inspectEnemy(enemy):
    print(enemy.name + " has " + str(enemy.health) + " health left.")
    print(enemy.name + " has " + str(enemy.armour) + " armour, and has an armor type of " + str(enemy.armourtype) + ".")
    print(enemy.name + " has " + str(enemy.dodge) + " dodge.")
    print(enemy.name + " has " + str(enemy.critical) + " critical chance.")