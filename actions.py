import time, random
from item_list import item_list, weapon_dict
from enemies import Enemy, enemies
from player import Player
from items import Item, Potion, Weapon
from constance import BOX_WIDTH, BUTTON_WIDTH
import ui

def show_menu(player):
    menu = True
    while menu:
        # options show_player_gear_and_inventory(), show_stats(), equip()
        print(f"|    {ui.print_button('1. Check Stats')}    {ui.print_button('2. Check Gear and Inventory')}    {ui.print_button('3. Equip')}    {ui.print_button('4. Depart')}   |")
        middle_padding = (BOX_WIDTH// 2)-1
        player_option = input(" " * middle_padding).strip().lower()
    
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
                elif confirm == ["no", "n"]:
                    break
                print("Choose: yes/no")



def take_a_rest(player):
    if player.current_health + round(player.max_health * 0.1) < player.max_health:
        player.current_health += round(player.max_health * 0.1)
    else:
        player.current_health = player.max_health
    print(player.current_health)
    return player.current_health