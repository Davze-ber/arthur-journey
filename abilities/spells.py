from abilities.abilities import Ability

import random

class FireBolt(Ability):
    def __init__(self):
        super().__init__(
            name = "Fire Bolt",
            tag = "damage",
            resource = "mana", 
            cost = 5,
            main_stat = "intelligence",
            second_stat = "intelligence", 
            primary_ratio = 1.5,
            secondary_ratio = 0,
            description =  "A searing bolt of flame"
            )
        
    
    def display_cost_damage(self,unit):
        dmg = self.calc_damage(unit)
        unit_int = unit.total_stats[self.main_stat]

        return f"{self.cost} {self.resource.capitalize()} {dmg} Damage (Int: {unit_int} x {self.primary_ratio} Spell Power: {unit.total_combat_stats['spell_power']})"
    

 