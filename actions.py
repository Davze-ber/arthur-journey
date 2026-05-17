import time, random, combat, enemies, actions
from item_list import item_list, weapon_dict
from player import Player
from items import Item, Potion, Weapon
from constance import BOX_WIDTH, BUTTON_WIDTH
import ui

def show_menu(player):
    menu = True
    while menu:
        # options show_player_gear_and_inventory(), show_stats(), equip()
        print(f"|    {ui.print_button('1. Check Stats')}    {ui.print_button('2. Check Gear and Inventory')}    {ui.print_button('3. Equip')}    {ui.print_button('4. Depart')}   |")
        middle_padding = (BOX_WIDTH// 2)-2
        player_option = input("|" +" " * middle_padding).strip().lower()
    
        if player_option == "1":
            ui.show_player_stats(player)
        elif player_option == "2":
            player.show_player_gear_and_inventory()
        elif player_option == "3":
            player.equip()
        elif player_option == "4":
            while True:
                confirm = input("Reade to explore the world: (yes/no)").strip().lower()
                if confirm in ["yes", "y"]:
                    menu = False
                    break
                elif confirm in ["no", "n"]:
                    break
                print("Choose: yes/no")
                time.sleep(1)


def take_a_rest(player):
    if player.current_health + round(player.max_health * 0.5) <= player.max_health:
        player.current_health += round(player.max_health * 0.5)
    else:
        player.current_health = player.max_health
    time.sleep(1)
    return player.current_health


def after_a_fight(player):
    after_a_fight = True
    while after_a_fight:
            player_decision = input("Do you want to to rest or continue?\n1: Check Stats 2: Show Gear and Inventory 3: Equip 4: Rest 5.Continue\nYour choise is: ")
            if player_decision == "1":
                ui.show_player_stats(player)
            elif player_decision == "2":
                player.show_player_gear_and_inventory()
            elif player_decision == "3":
                player.equip()
            elif player_decision == "4":
                actions.take_a_rest(player)
                after_a_fight = False
                time.sleep(1)
            elif player_decision == "5":
                after_a_fight = False
                time.sleep(1)