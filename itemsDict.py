from items import Item, Potion, Weapon




item_list = {
   "Lesser Potion" : lambda: Potion("Lesser Healing Potion", "Potion", "Health", value=10, healing_amount=5),
   "Strong Potion" : lambda: Potion("Strong Healing Potion", "Potion", "Health", value=10, healing_amount=10),
   "Lesser Mana Potion" : lambda: Potion("Lesser Mana Potion", "Potion", "Mana", value=10, restore_mana=5)
   }

weapon_dict = {
    "Wood Stick" : lambda: Weapon("Wooden Stick", "Weapon", "Main-Hand", 0, damage=1),
    "Axe" : lambda: Weapon("Axe", "Weapon", "Two-Hand", 10, damage=2),
}


armor_dict = {
    
}


