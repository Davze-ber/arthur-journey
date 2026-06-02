import time, random, combatMechanics, enemies, playerActions, maps
from itemsDict import item_list, weapon_dict
from playerCharacter import Player
from items import Item, Potion, Weapon, Armor, Equippable
from constance import BOX_WIDTH, BUTTON_WIDTH
from character import Character
from enemies import Enemy
from playerCharacter import Player
import visuals
from maps import world_map
 
def show_menu(player):
    menu = True
    while menu:
        # options show_player_gear_and_inventory(), show_stats(), equip()
        visuals.print_menu("1. Show Stats", "2. Show Inv", "3. Gear & Equip", "4. Depart")
        print(f"{visuals.bot_border_char*BOX_WIDTH}")
        player_option = input().center(BOX_WIDTH ).strip().lower()
        print(f"{visuals.top_border_char*BOX_WIDTH}")
        if player_option == "1":
            visuals.show_unit_stats_buffs_debuffs(player)
        elif player_option == "2":
            visuals.show_inventory(player)
        elif player_option == "3":
            while True:
                visuals.show_unit_gear_inv(player, player)
                visuals.print_menu("1. Change Character", "2. Equiq Item", "3. Unequip Item", "4. Back")
                player_choice = input(">")
                if player_choice == "1":
                    pass
                elif player_choice == "2":
                    equippable_lst = list(filter(lambda item : isinstance(item, Equippable), player.backpack))
                    print([equippable_lst])
                    player_equip_choice = input()
                elif player_choice == "3":
                    pass
                elif player_choice == "4":
                    break

        elif player_option == "4":
            visuals.print_titles("World Map")
            visuals.show_available_locations(world_map)
                
            map_choice = int(input("Where to go?: ")) -1 
            maps_lst = list(world_map.keys())
            selected_map = maps_lst[map_choice]


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

        gear_slot_item = None
        item_index = int(input("What item to equip?"))
        item_in_backpack = unit.backpack.index(item_index)
        chosen_item = unit.backpack[item_in_backpack]

        if isinstance(chosen_item, Weapon):
            if unit.gear["main_hand"] == None:
                unit.gear["main_hand"] = chosen_item
                unit.backpack.pop(item_index-1)
            else:
                gear_slot_item = unit.gear["main_hand"]
                unit.gear["main_hand"] = chosen_item
                unit.backpack.pop(item_index-1)
                unit.backpack.append(gear_slot_item)

        elif isinstance(chosen_item, Armor):
            if unit.gear["main_hand"] == None:
                unit.gear["main_hand"] = chosen_item
                unit.backpack.pop(chosen_item)
            else:
                gear_slot_item = unit.gear["main_hand"]
                unit.gear["main_hand"] = chosen_item
                unit.backpack.pop(item_index-1)
                unit.backpack.append(gear_slot_item)        



def after_a_fight(player):
    after_a_fight = True
    while after_a_fight:
            player_decision = input("Do you want to to rest or continue?\n1: Check Stats 2: Show Gear and Inventory 3: Equip 4: Rest 5.Continue\nYour choise is: ")
            if player_decision == "1":
                visuals.print_row(player)
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