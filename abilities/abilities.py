from constance import MIN_DAMAGE, MAX_DAMAGE
import random, math
class Ability():
    def __init__(self, name: str, tag: str, resource: str, cost: int, main_stat: str = 0, second_stat:str = 0, primary_ratio: float = 0, secondary_ratio:float = 0, description: str = ""):
        self.name = name
        self.tag = tag
        self.resource  = resource 
        self.cost = cost
        self.main_stat = main_stat
        self.second_stat = second_stat
        self.primary_ratio = primary_ratio
        self.secondary_ratio = secondary_ratio
        self. description = description


    @property
    def category(self) -> str:
        if self.main_stat in ["strenght, agility"]:
            return "Physical"
        elif self.main_stat == "intelligence":
            return "Magical"
        else:
            return "Other"

    
    def calc_damage(self, unit) -> int:
        bonus_damage = 0
        weapon_power = unit.total_combat_stats["weapon_power"]+ unit.weapon_damage
        spell_power = unit.total_combat_stats["spell_power"]
        primary_value = unit.total_stats[self.main_stat] * self.primary_ratio
        secondary_value = unit.total_stats[self.second_stat] * self.secondary_ratio
        
        if unit.resource_type in ["rage", "energy"]: 
            bonus_damage = weapon_power
          
        if unit.resource_type in ["mana"]:
            bonus_damage = spell_power
        else:
            bonus_damage = weapon_power + spell_power

        damage = primary_value + secondary_value + bonus_damage

        min_damage = int(max(1, math.floor(damage * MIN_DAMAGE)))
        max_damage = int(round(damage * MAX_DAMAGE))
        return min_damage, max_damage

    def can_cast(self, unit) -> bool:
        return unit.current_resource >= self.cost

    def apply_cost(self, unit) -> None:
        unit.current_resource = max(0, unit.current_resource - self.cost) 

    def deal_damage(self,caster, target) -> None:
        min_damage, max_damage = self.calc_damage(caster)
        incoming_damage = random.randint(min_damage,max_damage)
        damage_taken = int(max(0, incoming_damage - target.total_stats["defense"]))
        target.current_health -= damage_taken
        if target.resource_type == "rage":
            target.rage_regeneration()
        print(f"{self.name} dealt {damage_taken} damage to {target.name}!")
        if target.current_health <= 0:
            target.current_health = 0
            target.is_alive = False