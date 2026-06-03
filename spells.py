from abilities import Ability

import random

class FireBolt(Ability):
    def __init__(self):
        super().__init__(
            name = "Fire Bolt",
            resource = "mana", 
            cost = 5,
            main_stat = "intelligence",
            second_stat = "intelligence", 
            primary_ratio = 1.5,
            secondary_ratio = 0,
            description =  "A searing bolt of flame"
            )
        
    def get_spell_power(self,unit):
        return getattr(unit.gear.get("main_hand"), "spell_power", 0)
    
    def display_cost_damage(self,unit):
        dmg = self.damage(unit)
        unit_int = unit.total_stats["intelligence"]

        return f"{self.cost} {self.resource.capitalize()} {dmg} Damage (Int: {unit_int} x {self.primary_ratio} Spell Power: {self.get_spell_power(unit)})"
    
    def deal_damage(self,caster, target):
        power = self.get_spell_power(caster)
        bonus_damage = caster.total_stats["intelligence"] * self.primary_ratio
        damage = power + bonus_damage
        incoming_damage = damage + random.randint(-2,+2)
        damage_taken = int(max(0, incoming_damage - target.total_stats["defense"]))
        target.current_health -= damage_taken
        print(f"{self.name} dealt {damage_taken} damage to {target.name}!")
        if target.current_health <= 0:
            target.current_health = 0
            target.is_alive = False