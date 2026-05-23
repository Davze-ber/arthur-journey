from character import Character
from items import Item, Weapon, Armor
from item_list import item_list, weapon_dict

class Enemy(Character):
   def __init__(self, name, health, strength,agility, intelligence, defence, speed, level, experience,resource_type, gold=0, loot=None):
       super().__init__(name, health, strength,agility, intelligence, defence, speed, level, experience,resource_type)
       self.faction = "enemy"
       self.inventory["gold"] = gold
       if loot:
              if isinstance(loot, list):
                     loot = [loot]
              for item in loot:
                     self.backpack.append(item)


enemies_dict = {
       "slime": lambda: Enemy("Slime", health=3, strength=1, agility=1, intelligence=1, defence=1, speed=1,level=1, experience=5, resource_type="rage", gold=1, loot=[item_list["Lesser Potion"]()]),
       "wolf": lambda: Enemy("Wolf", health=5, strength=3, agility=1, intelligence=1, defence=1, speed=3, level=1,experience=10,resource_type="rage", gold=1, loot=None),
       "goblin": lambda: Enemy("Goblin", health=20, strength=8, agility=1, intelligence=1, defence=6, speed=3, level=1, experience=5,resource_type="rage", gold=10, loot=None)
}


