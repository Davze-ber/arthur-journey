import random
from character import Character


class Enemy(Character):
   def __init__(self, name, max_health, power, defence, speed, level, experience, ):
       super().__init__(name, max_health, power, defence, speed, level, experience)
       self.loot = None






enemies = [
       Enemy("Slime", 5, 3, 1, 1,1, 5),
       Enemy("Wolf", 12, 4, 1, 5, 1,10),
       Enemy("Goblin", 20, 8, 6, 3, 1, 5)
]




enemies_T1 = [
       Enemy("Slime", 5, 3, 1, 1,1, 5),
       Enemy("Wolf", 12, 4, 1, 5, 1,10),
]
enemies_T1_Boss = [Enemy("Goblin", 20, 8, 6, 3, 1, 5)]







