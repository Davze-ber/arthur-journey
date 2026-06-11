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
            secondary_ratio = 0.25,
            description =  "Hit the opponent with your head"
            )
    


 