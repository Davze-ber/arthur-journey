from items import Item, Potion, Weapon, Material, Junk

material_lst = {
    "Wolf Fur" : lambda: Material("Wolf Fur", "crafting", "material",can_stack=True, value=2)
}

junk_lst = {
    "Slime Gel" : lambda: Junk("Slime Gel", "junk", "junk",can_stack=True, value=1)
}

item_lst = {
   "Lesser Potion" : lambda: Potion("Lesser Healing Potion", "Potion", "health", value=10, healing_amount=5),
   "Strong Potion" : lambda: Potion("Strong Healing Potion", "Potion", "health", value=20, healing_amount=10),
   "Lesser Mana Potion" : lambda: Potion("Lesser Mana Potion", "Potion", "mana", value=10, restore_mana=5)
   }

weapon_dict = {
    "Wood Stick" : lambda: Weapon("Wooden Stick", "weapon", "main_hand", 0, weapon_damage=1),
    "Axe" : lambda: Weapon("Axe", "weapon", "main_hand", 10, weapon_damage=2),
}


armor_dict = {
    
}

shield_dict = {
    "Small Shield" : lambda: Weapon(name="Small Shield", category="shield", tag="off_hand", value=0, block_chance=5),
}
