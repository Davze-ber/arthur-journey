import time, random, visuals, enemies
import playerActions, combatMechanics
from itemsDict import item_list, weapon_dict
from enemies import enemies_dict
from playerCharacter import Player
from items import Item, Potion, Weapon
from constance import BOX_WIDTH, BUTTON_WIDTH




visuals.print_top_layer()
print(visuals.print_titles("Welcome!"))
print(visuals.print_titles("Nice to meet you, Arthur!"))
print(visuals.print_titles("Are you ready to go on the adventure?"))

# class Counter:
#     def __init__(self):
#         self.turn = 0
#     def increment_turn(self):
#         self.turn += 14

#         return self.turn

# Player Stats
player = Player(name="Arthur", resource_type="mana", health=5,strength=3,agility=1, intelligence=2, defense=2,speed=2,level=1,experience=0)

playerActions.show_menu(player)









 