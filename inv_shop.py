class itemdescription:
    def __init__(self, name, price, description, heal):
        self.name = name
        self.price = price
        self.description = description
        self.heal = heal
    
    

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
        
