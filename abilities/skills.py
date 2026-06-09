from abilities.abilities import Ability

import random

class HeadButt(Ability):
    def __init__(self):
        super().__init__(
            name = "HeadButt",
            tag = "damage",
            resource = "rage", 
            cost = 4,
            main_stat = "strength",
            second_stat = "health", 
            primary_ratio = 1,
            secondary_ratio = 0.5,
            description =  "Hit the opponent with your head"
            )
        
    
    def display_cost_damage(self,unit):
        dmg = self.calc_damage(unit)
        unit_int = unit.total_stats[self.main_stat]

        return f"{self.cost} {self.resource.capitalize()} {dmg} Damage (Int: {unit_int} x {self.primary_ratio} Spell Power: {unit.total_combat_stats['spell_power']})"
    

 