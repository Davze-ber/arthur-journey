from items import Item, Potion, Weapon




item_list = {
   "Lesser Potion" : lambda: Potion("Lesser Healing Potion", "Potion", "Health", value=10, healing_amount=5),
   "Strong Potion" : lambda: Potion("Strong Healing Potion", "Potion", "Health", value=10, healing_amount=10),
   "Lesser Mana Potion" : lambda: Potion("Lesser Mana Potion", "Potion", "Mana", value=10, restore_mana=5)
   }

weapon_dict = {
    "Wood Stick" : lambda: Weapon("Wooden Stick", "weapon", "main_hand", 0, weapon_damage=1),
    "Axe" : lambda: Weapon("Axe", "weapon", "main_hand", 10, weapon_damage=2),
}


armor_dict = {
    
}


