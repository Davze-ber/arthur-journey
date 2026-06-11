from entities.character import Character
from abilities.skills import HeadButt
from items import Item, Weapon, Armor
from itemsDict import item_lst, weapon_dict, material_lst,junk_lst

class Enemy(Character):
   def __init__(self, name:str , resource_type: str, health: int, strength: int, agility: int, intelligence: int, defense: int, speed: int, level: int, experience: int, gold:int = 0, loot: list[dict] = None, spellbook: list[dict] = None):
       super().__init__(name, resource_type, health, strength,agility, intelligence, defense, speed, level, experience)
       self.faction = "enemy"
       self.inventory["gold"] = gold
       self.loot = loot
       self.spellbook = spellbook

enemies_dict = {
       "slime": lambda: Enemy("Slime", resource_type="rage", health=3, strength=1, agility=1, intelligence=1, defense=1, speed=1,level=1, experience=5, gold=1, loot=[junk_lst["Slime Gel"]()], spellbook = [HeadButt()]),
       "wolf": lambda: Enemy("Wolf", resource_type="rage", health=5, strength=3, agility=1, intelligence=1, defense=1, speed=3, level=1,experience=10, gold=1, loot=[material_lst["Wolf Fur"]()]),
       "goblin": lambda: Enemy("Goblin", resource_type="rage", health=20, strength=8, agility=1, intelligence=1, defense=6, speed=3, level=1, experience=5, gold=10, loot=None)
}



