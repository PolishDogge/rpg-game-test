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
    armourpercentage = round((1-(1/(0.005*armour+1)))*10, 2)
    match armourtype:
        case 0:
            if armourpercentage > 0.05:
                armourpercentage = 0.05
        case 1:
            if armourpercentage > 0.15:
                armourpercentage = 0.15
        case 2:
            if armourpercentage > 0.25:
                armourpercentage = 0.25
        case 3:
            if armourpercentage > 0.35:
                armourpercentage = 0.35
        case 4:

            if armourpercentage > 0.55:
                armourpercentage = 0.55
    return armourpercentage

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


def fighting(character, room):
#make the player fight the enemy in the room
    for i in room.enemies:
        print("You have encountered a " + i.name + "!")
    