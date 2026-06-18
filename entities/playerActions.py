from items_inventory.items import Item, Potion, Weapon, Armor, Equippable
from ui_constance import BOX_WIDTH, BUTTON_WIDTH
from entities.enemies import Enemy
from entities.playerCharacter import Player

from maps import world_map

import time, random, combatMechanics, maps
import ui_components.ui_frames as ui_frames
import ui_components.ui_player as ui_player
import ui_components.ui_map as ui_map
 
def show_menu(player):
    menu = True
    while menu:
        # options show_player_gear_and_inventory(), show_stats(), equip()
        ui_frames.get_menu("Show Stats", "Show Inv", "Gear", "Town","Depart")
        print(f"{ui_frames.bot_border_char*BOX_WIDTH}")
        player_option = input().center(BOX_WIDTH ).strip().lower()
        print(f"{ui_frames.top_border_char*BOX_WIDTH}")
        if player_option == "1":
            ui_player.print_stats_table(player)
        elif player_option == "2":
            ui_player.print_inventory(player)
        elif player_option == "3":
            while True:
                ui_player.print_gear_equippable(player)
                ui_frames.print_menu("1. Change Character", "2. Equiq Item", "3. Unequip Item", "4. Back")
                player_choice = input(">")
                if player_choice == "1":
                    pass
                elif player_choice == "2":
                    equip(player)
                elif player_choice == "3":
                    pass
                elif player_choice == "4":
                    break
            
        elif player_option == "5":
            ui_map.show_available_locations(world_map)
            while True:
                print(f"Where to go?                                          X. Back ")
                player_choice = input(">")
                if player_choice.lower() == "x":
                    break
                elif player_choice.isdigit():
                    map_choice = int(player_choice) - 1
                    maps_lst = list(world_map.keys())
                    selected_map = maps_lst[map_choice]
                else:
                    print("Choose map or return")
                combatMechanics.enter_the_map(player, player.allies, selected_map)
            # while True:
            #     confirm = input("Reade to explore the world: (yes/no)").strip().lower()
                
            #     if confirm in ["yes", "y"]:
            #         menu = False
            #         break
            #     elif confirm in ["no", "n"]:
            #         break
            #     print("Choose: yes/no")
            #     time.sleep(1)


def equip(unit):
        gear_lst = list(filter(lambda item: isinstance(item, Equippable), unit.backpack))

        item_index = int(input("What item to equip?"))-1
        item_in_gear_lst = gear_lst[item_index] 
        item_in_backpack = unit.backpack.index(item_in_gear_lst)
        chosen_item = unit.backpack[item_in_backpack]

        gear_slot = chosen_item.tag
           
        old_gear_item = unit.gear[gear_slot]
        unit.backpack.pop(item_in_backpack)
        unit.gear[gear_slot] = chosen_item

        if old_gear_item is not None:
            unit.backpack.append(old_gear_item)        

def after_a_fight(player):
    after_a_fight = True
    while after_a_fight:
            player_decision = input("Do you want to to rest or continue?\n1: Check Stats 2: Show Gear and Inventory 3: Equip 4: Rest 5.Continue\nYour choise is: ")
            if player_decision == "1":
                ui_player.show_unit_stats_buffs_debuffs(player)
            elif player_decision == "2":
                ui_player.show_inventory(player)
            elif player_decision == "3":
                player.equip()
            elif player_decision == "4":
                player.take_a_rest()
                after_a_fight = False
                time.sleep(1)
            elif player_decision == "5":
                after_a_fight = False
                time.sleep(1)

