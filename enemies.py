from character import Character
from items import Item, Weapon, Armor
from itemsDict import item_list, weapon_dict

class Enemy(Character):
   def __init__(self, name:str , resource_type: str, health: int, strength: int, agility: int, intelligence: int, defence: int, speed: int, level: int, experience: int, gold:int = 0, loot: list[dict] = None):
       super().__init__(name, resource_type, health, strength,agility, intelligence, defence, speed, level, experience)
       self.faction = "enemy"
       self.inventory["gold"] = gold
       if loot:
              if isinstance(loot, list):
                     loot = [loot]
              for item in loot:
                     self.backpack.append(item)


enemies_dict = {
       "slime": lambda: Enemy("Slime", resource_type="rage", health=3, strength=1, agility=1, intelligence=1, defence=1, speed=1,level=1, experience=5, gold=1, loot=[item_list["Lesser Potion"]()]),
       "wolf": lambda: Enemy("Wolf", resource_type="rage", health=5, strength=3, agility=1, intelligence=1, defence=1, speed=3, level=1,experience=10, gold=1, loot=None),
       "goblin": lambda: Enemy("Goblin", resource_type="rage", health=20, strength=8, agility=1, intelligence=1, defence=6, speed=3, level=1, experience=5, gold=10, loot=None)
}



