import time, random, combat, enemies, actions, maps
from item_list import item_list, weapon_dict
from player import Player
from items import Item, Potion, Weapon
from constance import BOX_WIDTH, BUTTON_WIDTH
import ui
 
def show_menu(player):
    menu = True
    while menu:
        # options show_player_gear_and_inventory(), show_stats(), equip()
        ui.print_menu("1. Show Stats", "2. Show Gear & Inv", "3. Equip", "4. Depart")
        print(f"{ui.bot_border_char*BOX_WIDTH}")
        player_option = input().center(BOX_WIDTH).strip().lower()
        print(f"{ui.top_border_char*BOX_WIDTH}")
        if player_option == "1":
            ui.print_row(player)
        elif player_option == "2":
            player.show_player_gear_and_inventory()
        elif player_option == "3":
            player.equip()
        elif player_option == "4":
            combat.enter_the_map(player,[], maps.plains)
            # while True:
            #     confirm = input("Reade to explore the world: (yes/no)").strip().lower()
                
            #     if confirm in ["yes", "y"]:
            #         menu = False
            #         break
            #     elif confirm in ["no", "n"]:
            #         break
            #     print("Choose: yes/no")
            #     time.sleep(1)





def after_a_fight(player):
    after_a_fight = True
    while after_a_fight:
            player_decision = input("Do you want to to rest or continue?\n1: Check Stats 2: Show Gear and Inventory 3: Equip 4: Rest 5.Continue\nYour choise is: ")
            if player_decision == "1":
                ui.print_row(player)
            elif player_decision == "2":
                player.show_player_gear_and_inventory()
            elif player_decision == "3":
                player.equip()
            elif player_decision == "4":
                player.take_a_rest()
                after_a_fight = False
                time.sleep(1)
            elif player_decision == "5":
                after_a_fight = False
                time.sleep(1)