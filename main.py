
from entities.enemies import enemies_dict
from entities.playerCharacter import Player
from items import Item, Potion, Weapon
from constance import BOX_WIDTH, BUTTON_WIDTH
import entities.playerActions as aP
import combatMechanics
import ui_components.ui_frames as ui_frames



ui_frames.print_top_layer()
ui_frames.print_titles("Welcome!")
ui_frames.print_titles("Nice to meet you, Arthur!")
ui_frames.print_titles("Are you ready to go on the adventure?")

# class Counter:
#     def __init__(self):
#         self.turn = 0
#     def increment_turn(self):
#         self.turn += 14

#         return self.turn4


# Player Stats
player = Player(name="Arthur", resource_type="mana", health=5,strength=1,agility=1, intelligence=1, defense=1,speed=1,level=1,experience=0)

aP.show_menu(player)









 