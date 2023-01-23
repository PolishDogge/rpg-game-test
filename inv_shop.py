from item_descriptions import *
class itemdescription:
    def __init__(self, name, price, description, heal, defence, type, tier):
        self.name = name
        self.price = price
        self.description = description
        self.heal = heal
        self.defence = defence
        self.type = type
        self.tier = tier


def use(player):
    for i in player.inventory:
        print("You have a " + i.name)
    item = input("What item do you want to use? ")
    item = item.upper()
    for i in player.inventory:
        if item.upper() == i.name.upper():
            if i.type == "Potion":
                player.health += i.heal
                if player.health > player.maxHealth:
                    player.health = player.maxHealth
                print("You healed " + str(i.heal) + " health!")
                player.inventory.remove(i)
            elif i.type == "Armor":
                player.armour += i.defence
                print("You equipped " + i.name + "!")
                player.inventory.remove(i)
            else:
                print("You can't use that item!") 
    


class shop:
    #def __init__(self, character):
    def shop(character):
        print("Welcome to the shop!")
        print("What would you like to buy today?")
        print("We have potions, armor, and weapons!")
        print("We can even upgrade your armor and weapons!")
        print("You have " + str(character.gold) + " gold.")
        print("Options: potions, upgrade")
        what = input(">>> ").lower()
        if what == "potions":
            for i in items:
                if i.type == "Potion":
                    print(i.name + " costs " + str(i.price) + " gold. " + i.description)
                    
            what = input("What would you like to buy? ")
            what = what.lower()
            match what:
                case items.potion.name.lower():
                    buy(character, items.potion)
                case items.big_potion.name.lower():
                    buy(character, items.big_potion)
                case items.super_potion.name.lower():
                    buy(character, items.super_potion)
                case items.god_potion.name.lower():
                    buy(character, items.god_potion)
            print("That's not a potion!")
            shop.shop(character)
            
        elif what == "upgrade":
            print("You have a ")
            for i in character.inventory:
                if i.type == "Armor" or "Weapon":
                    print(i.name + " " + i.type + "")
            what = input("What would you like to upgrade? ")
            
            upgrade(character, what)
        
def upgrade(player, item):
    if item.name in player.inventory:
        if player.gold >= item.tier + 1:
            player.gold -= item.tier + 1
            item.tier += 1
            print("You upgraded your " + item.name + "!")
            print("It is now tier " + str(item.tier) + ".")
        else:
            print("You don't have enough gold!")
    else:
        print("You don't have that item!")
    shop.shop(player)

def buy(player, item):
    if player.gold >= item.price:
        player.gold -= item.price
        player.inventory.append(item.name)
        print("You bought a " + item.name)
    else:
        print("You don't have enough gold!")
    shop.shop(player)

#def sell(player, item):
#    if item in player.inventory:
#        player.gold += item.price
#        player.inventory.remove(item)
#        print("You sold a " + item.name)
#    else:
#        print("You don't have that item!")
#    shop.shop(player)