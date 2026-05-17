import random
from character import Character


class Enemy(Character):
   def __init__(self, name, max_health, power, defence, speed, level, experience, gold):
       super().__init__(name, max_health, power, defence, speed, level, experience)
       self.faction = "enemy"
       self.gold = gold
       self.loot = None



slime= Enemy("Slime", max_health=3, power=1, defence=1, speed=1,level=1, experience=5, gold=1)
wolf= Enemy("Wolf", max_health=5, power=3, defence=1, speed=3, level=1,experience=10, gold=1)
enemies_dict = {
       "slime": lambda: Enemy("Slime", max_health=3, power=1, defence=1, speed=1,level=1, experience=5, gold=1),
       "wolf": lambda: Enemy("Wolf", max_health=5, power=3, defence=1, speed=3, level=1,experience=10, gold=1),
       "goblin": lambda: Enemy("Goblin", max_health=20, power=8, defence=6, speed=3, level=1, experience=5, gold=10)
}


# forest_enemy = [slime, wolf, golbin]

# enemies_T1 = [
#        Enemy("Slime", 3, 2, 1, 1,1, 5,1),
#        # Enemy("Wolf", 5, 2, 1, 5, 1,10),
# ]
# enemies_T1_Boss = [Enemy("Goblin", 20, 8, 6, 3, 1, 5)]



# goblin = Enemy("Goblin", 20, 8, 6, 3, 1, 5)



