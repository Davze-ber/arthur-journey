import random
from typing import Any
from items import Item, Weapon, Potion, Armor
from constance import MIN_DAMAGE, MAX_DAMAGE
from abilities.skills import HeadButt
 
stats_lst: list[str] = ["health", "strength", "agility", "intelligence", "defense", "speed"]
combat_stats_lst: list[str] = ["weapon_power", "spell_power", "crit_chance", "crit_damage", "dodge_chance", "block_chance"]
regen_lst = ["rage", "energy" , "mana"]

class Character:
    def __init__(self, name: str, resource_type: str,
                 health: int = 0,strength: int = 0, agility: int = 0, intelligence: int = 0, defense: int = 0, speed: int = 0, level: int = 0, experience: int = 0):
        self.name = name
        self.is_alive: bool = True
        self.is_stunned: bool = False
        self.faction: str | None = None
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

        self.combat_stats: dict[str,int] = {
            "weapon_power" : 0,
            "spell_power" : 0,
            "crit_chance" : 5,
            "crit_damage" : 1.5,
            "dodge_chance" : 0,
            "block_chance" : 0
        }

        self.res_regen: dict[str,int] = {
            "rage" : 2,
            "energy" : 20,
            "mana" : 1
        }

        self.gear: dict[str, Equippable | None] = {
            "head": None,
            "neck": None,
            "chest": None,
            "legs": None,
            "main_hand": None,
            "off_hand":None,
                    }
        self.inventory: dict[str,Any] = {
            "gold"    : 0,
            "backpack": []
        }
        self.buff_lst: list[Any] = []    
        self.debuff_lst: list[Any] = []
        self.spellbook: list[Any] = []

        self._current_health: int = self.total_stats["health"]
        
        if self.resource_type == "rage":
            self._current_resource = 0
        else:
            self._current_resource = self.max_resource
    @property
    def current_health(self):
        return self._current_health

    @current_health.setter
    def current_health(self, value):
        if value <= 0:
            self._current_health = 0
            self.is_alive = False
        elif value > self.max_health:
            self._current_health = self.max_health
        else:
            self._current_health = value

    @property
    def current_resource(self):
        return self._current_resource

    @current_resource.setter
    def current_resource(self,value):
        if value < 0:
            self._current_resource = 0
        elif value > self.max_resource:
            self._current_resource = self.max_resource
        else:
            self._current_resource = value

    @property
    def max_resource(self) -> int:
        if self.resource_type == "rage":
            return 100
        
        if self.resource_type == "energy":
            return 120

        if self.resource_type == "mana":
            intelligence_increase = int(self.total_stats["intelligence"]*5)
            return self.base_mana + intelligence_increase
        return 100

    @property
    def bonus_res_regen(self):
        bonus_res_regen: dict[str,int] = {
            "rage" : 0,
            "energy" : 0,
            "mana" : 0
            }

        bonus_res_regen["mana"] += int(self.total_stats["intelligence"] * 0.25)
        return bonus_res_regen

    @property
    def total_res_regen(self) -> dict[str, int]:
        bonus_res_regen = self.bonus_res_regen
        return  {res: self.res_regen[res] + bonus_res_regen[res] for res in regen_lst}

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

        bonus_stats["health"] += int((self.core_stats["strength"] + bonus_stats["strength"]) * 2)

        defense_strength = (self.core_stats["strength"] + bonus_stats["strength"]) * 0.5
        defense_agility = (self.core_stats["agility"] + bonus_stats["agility"]) * 0.25
        bonus_stats["defense"] += int(defense_strength + defense_agility)

        bonus_stats["speed"] +=  int((self.core_stats["agility"] + bonus_stats["agility"]) * 0.25)
        return bonus_stats           

    @property
    def total_stats(self) -> dict[str, int]:
        bonus_stats = self.bonus_stats
        return  {stat: self.core_stats[stat] + bonus_stats[stat] for stat in stats_lst}
     
    @property 
    def max_health(self) -> int:
        return self.total_stats["health"] 

    @property
    def bonus_combat_stats(self):
        bonus_combat_stats: dict[str,int] = {
            "weapon_power" : 0,
            "spell_power" : 0,
            "crit_chance" : 0,
            "crit_damage" : 0,
            "dodge_chance" : 0,
            "block_chance" : 0
        }

        for slot, item in self.gear.items():
            if item:
                for combat_stat in combat_stats_lst:
                    bonus_combat_stats[combat_stat] += getattr(item, combat_stat, 0)

        bonus_combat_stats["weapon_power"] += (self.total_stats["strength"] * 0.5 + self.total_stats["agility"] * 0.25)
        bonus_combat_stats["spell_power"] += (self.total_stats["intelligence"] * 0.5)

        return bonus_combat_stats

    @property
    def total_combat_stats(self) -> dict[str, int]:
        bonus_combat_stats = self.bonus_combat_stats
        return {combat_stat: self.combat_stats[combat_stat] + bonus_combat_stats[combat_stat] for combat_stat in combat_stats_lst}

    @property
    def weapon_damage(self):
        main_hand = self.gear.get("main_hand")
        bonus_weapon_damage = getattr(main_hand, "weapon_damage", 0)
        return bonus_weapon_damage

    @property
    def backpack(self) -> list[Any]:
        return self.inventory["backpack"]
    
    @property
    def gold(self) -> int:
        return self.inventory["gold"]

    def gain_experience(self, total_exp):
        self.experience += total_exp

    def choose_the_target(self,player_team, enemy_team) -> list:
        
        if self.faction == "player" or  self.faction == "ally":
            target = enemy_team[0]
          
        elif self.faction == "enemy":
            target = player_team[0]
        if len(self.spellbook) >0 :
            for spell in self.spellbook:
                if spell.can_cast(self):
                    spell.deal_damage(self, target)
                    spell.apply_cost(self)
                    spell.display_cost_damage(self)
                    break
        else:
            self.basic_attack(target)
        return [target]


    def basic_attack(self, target) -> None:
        damage = self.weapon_damage   + self.total_combat_stats["weapon_power"]
        min_damage = int(max(0, damage * MIN_DAMAGE))
        max_damage = int(damage * MAX_DAMAGE)
        incoming_damage =  random.randint(min_damage, max_damage)
        damage_taken = max(0, incoming_damage - target.total_stats["defense"])
        target.current_health -= damage_taken
        target.rage_regeneration()
        print(f"{self.name} dealt {damage_taken} damage to {target.name}!")
        if target.current_health <= 0:
            target.current_health = 0
            target.is_alive = False

    def apply_potion_effect(self, source) -> None:
        if source.tag == "Rejuvenation" :
            heal_amount = getattr(source, "healing_amount", 0)
            self.current_health += heal_amount

            if self.resource_type == "mana":
                mana_amount = getattr(source, "restore_mana", 0)
                self.current_resource += mana_amount

        elif source.tag == "Health":
            heal_amount = getattr(source, "healing_amount", 0)
            self.current_health += heal_amount

        elif source.tag == "Mana":
            if self.resource_type == "mana":
                mana_amount = getattr(source, "restore_mana", 0)
                self.current_resource += mana_amount

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

        if chosen_potion.tag == "rejuvenation":
            print(f"{self.name} use {chosen_potion.name} and healed {chosen_potion.healing_amount}: and restored {chosen_potion.restore_mana}")
        elif chosen_potion.tag == "health":
            print(f"{self.name} use {chosen_potion.name} and healed {chosen_potion.healing_amount}:")
        elif chosen_potion.tag == "mana":
            print(f"{self.name} use {chosen_potion.name} and restored {chosen_potion.restore_mana}:")
        return True

    def resource_regeneration(self):
        regen_amount = self.total_res_regen.get(self.resource_type, 0)
        self.current_resource += regen_amount

    def rage_regeneration(self):
        if self.resource_type == "rage":
            bonus_rage = 2
            self.current_resource += self.total_res_regen["rage"] + bonus_rage
        

        

def chance(success_rate: int) -> bool:
    return random.random() * 100 <= success_rate


