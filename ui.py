from constance import BOX_WIDTH, BUTTON_WIDTH, MIDDLE_SPACE,COLUMN_SPACE,STATS_SPACE,TITLE_SPACE, NAME_SPACE, TURN_SPACE, DESCRIPTION_SPACE, DESCRIPTION_NAME
from itertools import zip_longest
from items import Armor, Weapon, Potion, Equippable
from playerCharacter import Player
import re,shutil
 
top_border_char = "▄"
bot_border_char = "▀"
border_width = BOX_WIDTH - 2
middle = BOX_WIDTH - 4
left_side = "█ "
right_side = " █"

RESET = "\033[0m"
BOLD_CYAN = "\033[1;36m"

def visible_length(text: str) -> int:
    """Remove ANSI codes to get real visible length"""
    return len(re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', text))

def print_top_layer():
    print(f"{top_border_char*BOX_WIDTH}")
    print(left_side + (middle * " ") + right_side)

def print_bot_layer():
    print(f"{bot_border_char*BOX_WIDTH}")

def print_titles(title):
  
    return f"{left_side}{title:^{middle}}{right_side}"




def print_button(text):
    leght_text = len(text)
    count_space = BUTTON_WIDTH - len(left_side + right_side + text)
    print(f"{top_border_char*15}",end="")
    print(f"{left_side}{text:^11}{right_side}", end="")
    print(f"{bot_border_char*15}", end="")
    
def print_menu(text1,text2,text3,text4):
    space = " " *5
    width_button = 27
    middle_button = 23
    print(f"{left_side}{space}{top_border_char*width_button}{space}{top_border_char*width_button}{space}{top_border_char*width_button}{space}{top_border_char*width_button}{space}{right_side}")

    print(f"{left_side}{space}{left_side}{text1:^{middle_button}}{right_side}{space}{left_side}{text2:^{middle_button}}{right_side}{space}{left_side}{text3:^{middle_button}}{right_side}{space}{left_side}{text4:^{middle_button}}{right_side}{space}{right_side}")

    print(f"{left_side}{space}{bot_border_char*width_button}{space}{bot_border_char*width_button}{space}{bot_border_char*width_button}{space}{bot_border_char*width_button}{space}{right_side}")
 

def show_unit_stats_buffs_debuffs(unit):
    middle_space = MIDDLE_SPACE
    middle_long_space = DESCRIPTION_NAME +2
    stats_space = STATS_SPACE
    title_space = TITLE_SPACE
    column_space = COLUMN_SPACE * " "

    top_part = f"╔{"═"*middle_space}╦{"═"*middle_space}╗"
    top_part_long = f"╔{"═"*middle_space}╦{"═"*middle_long_space}╦{"═"*7}╗"
    middle_part = f"╠{"═"*middle_space}╬{"═"*middle_space}╣"
    middle_part_long = f"╠{"═"*middle_space}╬{"═"*middle_long_space}╬{"═"*7}╣"
    bot_part = f"╚{"═"*middle_space}╩{"═"*middle_space}╝"
    bot_part_long = f"╚{"═"*middle_space}╩{"═"*middle_long_space}╩{"═"*7}╝"

    # Titles Attibutes Buffs Debuffs
    stats_title_part =  f"║ {"Attributes":^{title_space}} ║ {"Total":^{title_space}} ║"
    buffs_title_part =  f"║ {"Buffs":^{title_space}} ║ {"Description":^{DESCRIPTION_NAME}} ║ {"Turns":^5} ║"
    debufs_title_part = f"║ {"Debuffs":^{title_space}} ║ {"Description":^{DESCRIPTION_NAME}} ║ {"Turns":^5} ║"
    print(f"{left_side}{" " * (middle)}{right_side}")
    print(f"{left_side}{column_space}{top_part}{column_space}{top_part_long}{column_space}{top_part_long}{column_space}{right_side}")
    print(f"{left_side}{column_space}{stats_title_part}{column_space}{buffs_title_part}{column_space}{debufs_title_part}{column_space}{right_side}")
    
    for stat_name, buff_obj, debuff_obj in zip_longest(unit.core_stats, unit.buff_lst, unit.debuff_lst):
        # Stats
        total_values = unit.total_stats.get(stat_name, 0)
        core_values = unit.core_stats.get(stat_name, 0)
        bonus_values = unit.bonus_stats.get(stat_name, 0)
        # Buffs
        if buff_obj:
            buff_name = buff_obj.name.capitalize()
            buff_descriptions = buff_obj.description
            buff_duration = buff_obj.duration
        else:
            buff_name = "---"
            buff_descriptions = "---"
            buff_duration = "---"

        # Debufss
        if buff_obj:
            debuff_name = debuff_obj.name.capitalize()
            debuff_descriptions = debuff_obj.description
            debuff_duration = debuff_obj.duration
        else:
            debuff_name = "---"
            debuff_descriptions = "---"
            debuff_duration = "---"
            
        # Middle Part
        stats_part =   f"║ {stat_name.capitalize():<{NAME_SPACE}}║ {total_values:^{stats_space}}({core_values:^{stats_space}}+{bonus_values:^{stats_space}}) ║"
        buffs_part =   f"║ {buff_name:<{NAME_SPACE}}║ {buff_descriptions:<{DESCRIPTION_SPACE}} ║ {buff_duration:^{TURN_SPACE}} ║"
        debuffs_part = f"║ {debuff_name:<{NAME_SPACE}}║ {debuff_descriptions:<{DESCRIPTION_SPACE}} ║ {debuff_duration:^{TURN_SPACE}} ║"
        print(f"{left_side}{column_space}{middle_part}{column_space}{middle_part_long}{column_space}{middle_part_long}{column_space}{right_side}")
        print(f"{left_side}{column_space}{stats_part}{column_space}{buffs_part}{column_space}{debuffs_part}{column_space}{right_side}")
        # Bottom Part

    print(f"{left_side}{column_space}{bot_part}{column_space}{bot_part_long}{column_space}{bot_part_long}{column_space}{right_side}")

def show_inventory(unit):
    equippable = [item for item in unit.inventory["backpack"] if isinstance(item, Equippable)]
    potions = [potion for potion in unit.inventory["backpack"] if isinstance(potion, Potion)] 

    index_equippable = [(i+1, item) for i, item in enumerate(equippable)]
    index_potions = [(i+1, potion) for i, potion in enumerate(potions)]
     
    for item, potion in zip_longest(index_equippable, index_potions):

        item_index, item_obj = item
        if item_obj:
            item_name = item_obj.name
            item_category = item_obj.category
            item_tag = item_obj.tag
            item_value = item_obj.value

#  XXXX IN PROGRESS XXXX
def show_unit_gear_inv(unit): 
    middle_space = MIDDLE_SPACE
    middle_long_space = DESCRIPTION_NAME +2
    stats_space = STATS_SPACE
    title_space = TITLE_SPACE
    column_space = COLUMN_SPACE * " "

    top_part = f"╔{"═"*middle_space}╦{"═"*middle_space}╗"
    top_part_long = f"╔{"═"*middle_space}╦{"═"*middle_long_space}╦{"═"*7}╗"
    middle_part = f"╠{"═"*middle_space}╬{"═"*middle_space}╣"
    middle_part_long = f"╠{"═"*middle_space}╬{"═"*middle_long_space}╬{"═"*7}╣"
    bot_part = f"╚{"═"*middle_space}╩{"═"*middle_space}╝"
    bot_part_long = f"╚{"═"*middle_space}╩{"═"*middle_long_space}╩{"═"*7}╝"

    # Titles Attibutes Buffs Debuffs
    gear_title_part =  f"║ {"Gear":^{title_space}} ║ {"Items":^{title_space}} ║"
    inventory_title_part =  f"║ {"Inventort":^{title_space}} ║"
    debufs_title_part = f"║ {"Debuffs":^{title_space}} ║ {"Description":^{DESCRIPTION_NAME}} ║ {"Turns":^5} ║"
    print(f"{left_side}{" " * (middle)}{right_side}")
    print(f"{left_side}{column_space}{top_part}{column_space}{top_part_long}{column_space}{top_part_long}{column_space}{right_side}")
    print(f"{left_side}{column_space}{gear_title_part}{column_space}{inventory_title_part}{column_space}{right_side}")
    
    for gear_obj, item, stat_name in zip_longest(unit.gear, unit.inventory["backpack"], unit.total_stats):
        # Unit Gear
        gear_name = gear_obj.name or "Empty"
        gear_weapon_damage = gear_obj.weapon or 0
        gear_health = gear_obj.health or 0
        gear_strength = gear_obj.strength or 0
        gear_agility = gear_obj.agility or 0
        gear_intelligence = gear_obj.intelligence or 0
        gear_defence = gear_obj.defence or 0
        gear_speed = gear_speed.speed or 0
        total_values = unit.core_stats.get(stat_name, 0)
     
        # Inventory
        item_name = item.name
       
       
            
        # Middle Part
        stats_part =   f"║ {gear_name.capitalize():<{NAME_SPACE}}║ {total_values:^{stats_space}} ║"
        # buffs_part =   f"║ {buff_name.capitalize():<{NAME_SPACE}}║ {buff_descriptions:<{DESCRIPTION_SPACE}} ║ {buff_duration:^{TURN_SPACE}} ║"
        # # debuffs_part = f"║ {debuff_name.capitalize():<{NAME_SPACE}}║ {debuff_descriptions:<{DESCRIPTION_SPACE}} ║ {debuff_duration:^{TURN_SPACE}} ║"
        # print(f"{left_side}{column_space}{middle_part}{column_space}{middle_part_long}{column_space}{middle_part_long}{column_space}{right_side}")
        # print(f"{left_side}{column_space}{stats_part}{column_space}{buffs_part}{column_space}{debuffs_part}{column_space}{right_side}")
        # Bottom Part

    print(f"{left_side}{column_space}{bot_part}{column_space}{bot_part_long}{column_space}{bot_part_long}{column_space}{right_side}")

player = Player(name="Arthur", resource_type="rage", health=999,strength=3,agility=1, intelligence=1, defence=2,speed=2,level=1,experience=0)

print(show_inventory(player))