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
            primary_ratio = 2,
            description =  "A searing bolt of flame"
            )
    
    def clone(self):
        return FireBolt()