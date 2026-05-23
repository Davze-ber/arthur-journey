import time, random, ui, enemies
import actions, combat
from item_list import item_list, weapon_dict
from enemies import enemies_dict
from player import Player
from items import Item, Potion, Weapon
from constance import BOX_WIDTH, BUTTON_WIDTH




ui.print_top_layer()
print(ui.print_titles("Welcome!"))
print(ui.print_titles("Nice to meet you, Arthur!"))
print(ui.print_titles("Are you ready to go on the adventure?"))

# class Counter:
#     def __init__(self):
#         self.turn = 0
#     def increment_turn(self):
#         self.turn += 1
#         return self.turn

# Player Stats
player = Player(name="Arthur", health=999,strength=3,agility=1, intelligence=1, defence=2,speed=2,level=1,experience=0, resource_type="rage")

actions.show_menu(player)

44

ui.print_bot_layer()

 


4









