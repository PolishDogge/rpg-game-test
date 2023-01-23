from inv_shop import itemdescription

class items:
    potion = itemdescription("Potion", 10, "A standard small potion that heals 40 health.",40,0,"Potion",1)
    big_potion = itemdescription("Big Potion", 50, "A standard big potion that heals 100 health.",100,0,"Potion",2)
    super_potion = itemdescription("Super Potion", 100, "A standard super potion that heals 200 health.",200,0,"Potion",3)
    god_potion = itemdescription("God Potion", 500, "The potion is a weird color of blue... heals 500 health.",500,0,"Potion",4)

    wooden_sword = itemdescription("Wooden sword", 100, "A standard wooden sword commonly used for training. Does 10 damage.",0,0,"Weapon",1)
    iron_sword = itemdescription("Iron sword", 500, "A very common iron sword that does 20 damage.",0,0,"Weapon",2)
    steel_sword = itemdescription("Steel sword", 1000, "A very common steel sword that does 30 damage.",0,0,"Weapon",3)
    darksteel_sword = itemdescription("Darksteel sword", 5000, "A very common darksteel sword that does 40 damage.",0,0,"Weapon",4)

    dagger = itemdescription("Dagger", 100, "A standard dagger that does 10 damage.",0,0,"Weapon",1)
    poison_dagger = itemdescription("Poison Dagger", 500, "A standard dagger that does 10 damage and poisons the enemy.",0,0,"Weapon",1)
    steel_dagger = itemdescription("Steel Dagger", 1000, "A standard steel dagger that does 20 damage.",0,0,"Weapon",2)
    darksteel_dagger = itemdescription("Darksteel Dagger", 5000, "A standard darksteel dagger that does 30 damage.",0,0,"Weapon",3)

    staff = itemdescription("Staff", 100, "A standard staff that does 10 damage.",0,0,"Weapon",1)
    fire_staff = itemdescription("Fire Staff", 500, "A standard staff that does 10 damage and sets the enemy on fire.",0,0,"Weapon",2)
    old_wood_staff = itemdescription("Old Wood Staff", 1000, "A very old staff that does 35 damage.",0,0,"Weapon",3)
    ancient_staff = itemdescription("Ancient Staff", 1000, "A very old staff that does 100 damage.",0,0,"Weapon",4)

    bow = itemdescription("Bow", 100, "A standard bow that does 10 damage.",0,0,"Weapon",1)
    old_bow = itemdescription("Old Bow", 500, "A very old bow that does 20 damage.",0,0,"Weapon",2)
    mechanical_bow = itemdescription("Mechanical Bow", 1000, "A very old bow that does 45 damage.",0,0,"Weapon",3)
    dark_bow = itemdescription("Dark Bow", 5000, "A very old, ancient even, bow that does 100 damage.",0,0,"Weapon",4)

    shield = itemdescription("Shield", 100, "A standard shield that gives you 5 armor.",0,5,"Armor",1)
    leather_armor = itemdescription("Leather Armor", 500, "A standard leather armor that gives you level 1 armor (and bonus armor).",0,10,"Armor",1)
    chainmail_armor = itemdescription("Chainmail Armor", 1000, "A standard chainmail armor that gives you level 2 armor (and bonus armor).",0,20,"Armor",1)
    steel_armor = itemdescription("Steel Armor", 5000, "A standard steel armor that gives you level 3 armor (and bonus armor).",0,35,"Armor",1)
    darksteel_armor = itemdescription("Darksteel Armor", 10000, "A standard darksteel armor that gives you level 4 armor (and bonus armor).",0,55,"Armor",1)

class forgeAssets:
    apple = (None,None,None,None,None,None)
    golden_apple = (None,None,None,None,None,None)
    
    
    diamond = (None,None,None,None,None,None)
    emerald = (None,None,None,None,None,None)
    ruby = (None,None,None,None,None,None)

    iron_ore = (None,None,None,None,None,None)
    coal = (None,None,None,None,None,None)
    gold_ore = (None,None,None,None,None,None)
    iron_ingot = (None,None,None,None,None,None)
    gold_ingot = (None,None,None,None,None,None)
    
    string = (None,None,None,None,None,None)
    stick = (None,None,None,None,None,None)
    leather = (None,None,None,None,None,None)
    wood = (None,None,None,None,None,None)
    
    expensive_gem = (None,None,None,None,None,None)
    low_value_gem = (None,None,None,None,None,None)
    medium_value_gem = (None,None,None,None,None,None)
    high_value_gem = (None,None,None,None,None,None)
    
class forge:
    def forge(item, character):
        match item:
            case "sword":
                if character.inventory["iron_ingot"] >= 2:
                    character.inventory["iron_ingot"] -= 2
                    character.inventory.append(items.sword)
                    print("You have forged an iron sword!")
                else:
                    print("You don't have enough iron ingots to forge an iron sword!")


            case "dagger":
                if character.inventory["iron_ingot"] >= 1:
                    character.inventory["iron_ingot"] -= 1
                    character.inventory.append(items.dagger)
                    print("You have forged an iron dagger!")
                else:
                    print("You don't have enough iron ingots to forge an iron dagger!")
            case "armor":
                if character.inventory["iron_ingot"] >= 3:
                    character.inventory["iron_ingot"] -= 3
                    character.inventory.append(items.armor)
                    print("You have forged iron armor!")
                else:
                    print("You don't have enough iron ingots to forge iron armor!")
            case "shield":
                if character.inventory["iron_ingot"] >= 2:
                    character.inventory["iron_ingot"] -= 2
                    character.inventory.append(items.shield)
                    print("You have forged an iron shield!")
                else:
                    print("You don't have enough iron ingots to forge an iron shield!")
            case "bow":
                if character.inventory["wood"] >= 3:
                    if character.inventory["string"] >= 2:
                        character.inventory["wood"] -= 3
                        character.inventory["string"] -= 2
                        character.inventory.append(items.bow)
                        print("You have forged a bow!")
                else:
                    print("You don't have enough iron ingots to forge an iron bow!")
            case "staff":
                if character.inventory["wood"] >= 5:
                    character.inventory["iron_ingot"] -= 5
                    character.inventory.append(items.staff)
                    print("You have forged an iron staff!")
                else:
                    print("You don't have enough iron ingots to forge an iron staff!")
            case "gem":
                if character.inventory["diamond"] >= 1:
                    character.inventory["diamond"] -= 1
                    character.inventory.append(items.expensive_gem)
                    print("You have forged an expensive gem!")
                elif character.inventory["emerald"] >= 1:
                    character.inventory["emerald"] -= 1
                    character.inventory.append(items.high_value_gem)
                    print("You have forged a high value gem!")
                elif character.inventory["ruby"] >= 1:
                    character.inventory["ruby"] -= 1
                    character.inventory.append(items.medium_value_gem)
                    print("You have forged a medium value gem!")
                elif character.inventory["coal"] >= 1:
                    character.inventory["coal"] -= 1
                    character.inventory.append(items.low_value_gem)
                    print("You have forged a low value gem!")

        print("You can't forge that!")