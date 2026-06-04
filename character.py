import random
from typing import Any
from items import Item, Weapon, Potion, Armor
from constance import MIN_DAMAGE, MAX_DAMAGE
 

stats_lst: list[str] = ["health", "strength", "agility", "intelligence", "defense", "speed"]

class Character:
    def __init__(self, name: str, resource_type: str,
                 health: int = 0,strength: int = 0, agility: int = 0, intelligence: int = 0, defense: int = 0, speed: int = 0, level: int = 0, experience: int = 0):
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
            "defense" : defense,
            "speed" : speed,
        }
        self.gear: dict[str,Any] = {
            "head": None,
            "neck": None,
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
        self.spellbook: list[Any] = []
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
            "defense" : 0,
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
    def weapon_power(self):
        main_hand = self.gear.get("main_hand")
        bonus_weapon_damage = getattr(main_hand, "weapon_power", 0)
        return bonus_weapon_damage

    @property
    def spell_power(self):
        main_hand = self.gear.get("main_hand")
        bonus_spell_damage = getattr(main_hand, "spell_power", 0)
        return bonus_spell_damage

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
        damage = self.total_stats["strength"] + self.weapon_damage
        min_damage = int(max(0, damage * MIN_DAMAGE))
        max_damage = int(damage * MAX_DAMAGE)
        incoming_damage =  random.randint(min_damage, max_damage)
        damage_taken = max(0, incoming_damage - target.total_stats["defense"])
        target.current_health -= damage_taken
        print(f"{self.name} dealt {damage_taken} damage to {target.name}!")
        if target.current_health <= 0:
            target.current_health = 0
            target.is_alive = False

    def apply_potion_effect(self, source) -> None:
        if source.tag == "Rejuvenation" :
            heal_amount = getattr(source, "healing_amount", 0)
            self.current_health = min(self.current_health + heal_amount, self.max_health)

            if self.resource_type == "mana":
                mana_amount = getattr(source, "restore_mana", 0)
                self.current_resource = min(self.current_resource + mana_amount, self.max_resource)

        elif source.tag == "Health":
            heal_amount = getattr(source, "healing_amount", 0)
            self.current_health = min(self.current_health + heal_amount, self.max_health)

        elif source.tag == "Mana":
            if self.resource_type == "mana":
                mana_amount = getattr(source, "restore_mana", 0)
                self.current_resource = min(self.current_resource + mana_amount, self.max_resource)

    def use_potion(self) -> bool:
        potions = list(filter(lambda item: isinstance(item, Potion), self.backpack))
        if not potions:
            print("You have no potions!")
            return False

        print("Potions in my inventory:")
        for i, potion in enumerate(potions, start=1):
            print(f"{i}: {potion.name}")


        index_of_potion = int(input("Choose the Potion: ")) -1 
        chosen_potion = potions[index_of_potion]
        
        self.apply_potion_effect(chosen_potion)
        self.backpack.remove(chosen_potion)

        if chosen_potion.tag == "Rejuvenation":
            print(f"{self.name} use {chosen_potion.name} and healed {chosen_potion.healing_amount}: and restored {chosen_potion.restore_mana}")
        elif chosen_potion.tag == "Health":
            print(f"{self.name} use {chosen_potion.name} and healed {chosen_potion.healing_amount}:")
        elif chosen_potion.tag == "Mana":
            print(f"{self.name} use {chosen_potion.name} and healed {chosen_potion.restore_mana}:")
        return True

        

def chance(success_rate: int) -> bool:
    return random.random() * 100 <= success_rate


