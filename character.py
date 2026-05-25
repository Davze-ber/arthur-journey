import random
from typing import Any
from items import Item, Weapon, Potion, Armor
 

stats_lst: list[str] = ["health", "strength", "agility", "intelligence", "defence", "speed"]

class Character:
    def __init__(self, name: str, resource_type: str,
                 health: int = 0,strength: int = 0, agility: int = 0, intelligence: int = 0, defence: int = 0, speed: int = 0, level: int = 0, experience: int = 0):
        self.name = name
        self.is_alive: bool = True
        self.is_stunned: bool = False
        self.faction: str = None
        self.experience = experience
        self.level = level
        self.resource_type = resource_type
        self.base_mana = 10


        self.core_stats: dict[str,int] = {
            "health" : health,
            "strength" : strength,
            "agility" : agility,
            "intelligence" : intelligence,
            "defence" : defence,
            "speed" : speed,
        }
        self.gear: dict[str,Any] = {
            "head": None,
            "chest": None,
            "legs": None,
            "main_hand": None,
            "off_hand":None,
                    }
        self.inventory: dict[str,Any] = {
            "gold" : 0,
            "backpack": []
        }
        self.buff_lst: list[Any] = []    
        self.debuff_lst: list[Any] = []

        self.current_health: int = self.total_stats["health"]
        if self.resource_type == "rage":
            self.current_resource = 0
        else:
            self.current_resource = self.max_resource
        
    @property
    def bonus_stats(self) -> dict[str,int]:
        bonus_stats = {
            "health" : 0,
            "strength" : 0,
            "agility" : 0,
            "intelligence" : 0,
            "defence" : 0,
            "speed" : 0,
        }
        for slot, item in self.gear.items():
            if item:
                for stat in stats_lst:
                    bonus_stats[stat] += getattr(item, stat, 0)
            
        for buff in self.buff_lst:
            if buff:
                for stat in stats_lst:
                    bonus_stats[stat] += getattr(buff, stat, 0)
          

        for debuff in self.debuff_lst:
            if debuff:
                for stat in stats_lst:
                    bonus_stats[stat] += getattr(debuff, stat, 0)

        return bonus_stats
                    
    @property
    def total_stats(self) -> dict[str, int]:
        bonus_stats = self.bonus_stats
        return {stat: self.core_stats[stat] + bonus_stats[stat] for stat in stats_lst}
        
    @property 
    def max_health(self) -> int:
        return self.total_stats["health"]

    @property
    def backpack(self) -> list[Any]:
        return self.inventory["backpack"]
    
    @property
    def gold(self) -> int:
        return self.inventory["gold"]

    @property
    def max_resource(self) -> int:
        if self.resource_type == "rage":
            return 100
        
        if self.resource_type == "energy":
            return 120

        if self.resource_type == "mana":
            intelligence_increase = int(self.total_stats["intelligence"] * 2)
            return self.base_mana + intelligence_increase

    
    def choose_the_target(self,player_team, enemy_team) -> list:
        if self.faction == "player" or  self.faction == "ally":
            target = enemy_team[0]
          
        elif self.faction == "enemy":
            target = player_team[0]

        self.basic_attack(target)
        return [target]


    def basic_attack(self, target) -> None:
        weapon = self.gear["main_hand"]
        if weapon:
            weapon_damage = getattr(weapon,"damage", 0)
        else:
            weapon_damage = 0
        incoming_damage = self.total_stats["strength"] + weapon_damage + random.randint(-2,+2)
        damage_taken = max(0, incoming_damage - target.total_stats["defence"])
        target.current_health -= damage_taken
        print(f"{self.name} dealt {damage_taken} damage to {target.name}!")
        if target.current_health <= 0:
            target.current_health = 0
            target.is_alive = False

  

    def use_potion(self) -> bool:
        potions = list(filter(lambda item: isinstance(item, Potion), self.backpack))
        if not potions:
            print("You have no potions!")
            return False

        print("Potions in my inventory:")
        for i, potion in enumerate(potions):
            print(f"{i + 1}: {potion.name}")


        index_of_potion = int(input("Choose the Potion: "))
        chosen_potion = potions[index_of_potion - 1]
        
        self.apply_healing(chosen_potion)
        self.backpack.remove(chosen_potion)


        print(f"{self.name} use {chosen_potion.name} and healed {chosen_potion.healing_amount}:")
        return True

        

def chance(success_rate: int) -> bool:
    return random.random() * 100 <= success_rate


def apply_healing(self, source) -> None:
    heal_amount = getattr(source, "healing_amount", 0)

    self.current_health = min(self.current_health + heal_amount, self.max_health)



