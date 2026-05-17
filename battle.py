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
player = Player(name="Arthur", max_health=5,power=3,defence=2,speed=2,level=1,experience=0)

actions.show_menu(player)
# player_alive = True
# while True:
#     for enemy in enemies:
#         combat.combat(player,ally = None, enemy)
#     if player.status == "Dead":
#         break

result = combat.combat(player, [], [enemies.slime,enemies.wolf])

if result == "Victory":
    actions.after_a_fight(player)
elif result == "Defeat":
    print("X" * BOX_WIDTH)
    print(f"{player.name} has survive the long journey!")
    print("X" * BOX_WIDTH)
    actions.show_menu(player)






ui.print_bot_layer()














