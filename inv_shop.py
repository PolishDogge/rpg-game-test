class itemdescription:
    def __init__(self, name, price, description, heal, defence, type):
        self.name = name
        self.price = price
        self.description = description
        self.heal = heal
        self.defence = defence
        self.type = type
    
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
    def shop(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
    def buy(self, player, item):
        if player.gold >= item.price:
            player.gold -= item.price
            player.inventory.append(item.name)
            print("You bought a " + item.name)
        else:
            print("You don't have enough gold!")
    
    def sell(self, player, item):
        if item.name in player.inventory:
            player.gold += item.price
            player.inventory.remove(item.name)
            print("You sold a " + item.name)
        else:
            print("You don't have that item!")
    
    def inspect(self, item):
        print(item.name + " costs " + str(item.price) + " gold. " + item.description)
        
