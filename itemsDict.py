from items import Item, Potion, Weapon




item_list = {
   "Lesser Potion" : lambda: Potion("Lesser Healing Potion", "Potion", "Health", 10, 5),
   "Strong Potion" : lambda: Potion("Strong Healing Potion", "Potion", "Health", 10, 10)
   }

weapon_dict = {
    "Wood Stick" : lambda: Weapon("Wooden Stick", "Weapon", "Main-Hand", 0, 1),
    "Axe" : lambda: Weapon("Axe", "Weapon", "Two-Hand", 10, 2),
}


armor_dict = {
    
}


