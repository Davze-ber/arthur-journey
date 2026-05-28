
from constance import BOX_WIDTH, BUTTON_WIDTH, MIDDLE_SPACE,COLUMN_SPACE,STATS_SPACE,TITLE_SPACE, NAME_SPACE, TURN_SPACE, DESCRIPTION_SPACE, DESCRIPTION_NAME, GEAR_SLOT, GEAR_ITEM, EQUIPPABLE_NAME
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
    space_side_w = " " *5
    space_middle_w = " " * 6
    width_button = 27
    middle_button = 23
    print(f"{left_side}{space_side_w}{top_border_char*width_button}{space_middle_w}{top_border_char*width_button}{space_middle_w}{top_border_char*width_button}{space_middle_w}{top_border_char*width_button}{space_side_w}{right_side}")

    print(f"{left_side}{space_side_w}{left_side}{text1:^{middle_button}}{right_side}{space_middle_w}{left_side}{text2:^{middle_button}}{right_side}{space_middle_w}{left_side}{text3:^{middle_button}}{right_side}{space_middle_w}{left_side}{text4:^{middle_button}}{right_side}{space_side_w}{right_side}")

    print(f"{left_side}{space_side_w}{bot_border_char*width_button}{space_middle_w}{bot_border_char*width_button}{space_middle_w}{bot_border_char*width_button}{space_middle_w}{bot_border_char*width_button}{space_side_w}{right_side}")
 

def show_unit_stats_buffs_debuffs(unit):
    middle_space_w = MIDDLE_SPACE
    middle_long_space_w = DESCRIPTION_NAME +2
    stats_space_w = STATS_SPACE
    title_space_w = TITLE_SPACE
    column_space_w = COLUMN_SPACE * " "
    column_space_longer_w = (COLUMN_SPACE +1) * " "
    top_part = f"╔{'═'*middle_space_w}╦{'═'*middle_space_w}╗"
    top_part_long = f"╔{'═'*middle_space_w}╦{'═'*middle_long_space_w}╦{'═'*7}╗"
    middle_part = f"╠{'═'*middle_space_w}╬{'═'*middle_space_w}╣"
    middle_part_long = f"╠{'═'*middle_space_w}╬{'═'*middle_long_space_w}╬{'═'*7}╣"
    bot_part = f"╚{'═'*middle_space_w}╩{'═'*middle_space_w}╝"
    bot_part_long = f"╚{'═'*middle_space_w}╩{'═'*middle_long_space_w}╩{'═'*7}╝"

    # Titles Attibutes Buffs Debuffs
    stats_title_part =  f"║ {'Attributes':^{title_space_w}} ║ {'Total':^{title_space_w}} ║"
    buffs_title_part =  f"║ {'Buffs':^{title_space_w}} ║ {'Description':^{DESCRIPTION_SPACE}} ║ {'Turns':^5} ║"
    debufs_title_part = f"║ {'Debuffs':^{title_space_w}} ║ {'Description':^{DESCRIPTION_SPACE}} ║ {'Turns':^5} ║"
    print(f"{left_side}{" " * (middle)}{right_side}")
    print(f"{left_side}{column_space_w}{top_part}{column_space_w}{top_part_long}{column_space_longer_w}{top_part_long}{column_space_w}{right_side}")
    print(f"{left_side}{column_space_w}{stats_title_part}{column_space_w}{buffs_title_part}{column_space_longer_w}{debufs_title_part}{column_space_w}{right_side}")
    
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
        stats_part =   f"║ {stat_name.capitalize():<{NAME_SPACE}}║ {total_values:^{stats_space_w}}({core_values:^{stats_space_w}}+{bonus_values:^{stats_space_w}}) ║"
        buffs_part =   f"║ {buff_name:<{NAME_SPACE}}║ {buff_descriptions:<{DESCRIPTION_SPACE}} ║ {buff_duration:^{TURN_SPACE}} ║"
        debuffs_part = f"║ {debuff_name:<{NAME_SPACE}}║ {debuff_descriptions:<{DESCRIPTION_SPACE}} ║ {debuff_duration:^{TURN_SPACE}} ║"
        print(f"{left_side}{column_space_w}{middle_part}{column_space_w}{middle_part_long}{column_space_longer_w}{middle_part_long}{column_space_w}{right_side}")
        print(f"{left_side}{column_space_w}{stats_part}{column_space_w}{buffs_part}{column_space_longer_w}{debuffs_part}{column_space_w}{right_side}")
        # Bottom Part

    print(f"{left_side}{column_space_w}{bot_part}{column_space_w}{bot_part_long}{column_space_longer_w}{bot_part_long}{column_space_w}{right_side}")

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
    gear_slot_w = GEAR_SLOT
    gear_slot_name_w = gear_slot_w - 2
    gear_item_name_w = GEAR_ITEM - 2
    
    equippable_slot_w = EQUIPPABLE_NAME
    equippable_slot_name_w = EQUIPPABLE_NAME - 2
    equippable_index_w = 3
    equippable_name_w = equippable_slot_w - 0
    stats_space_w = STATS_SPACE +2 
    column_space_w = COLUMN_SPACE * " "

    # Info for Gear and Equippable
    stat_info_top =    f"{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╗"
    stat_info_middle = f"{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╣"
    stat_info_bottom = f"{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╝"
    # Labels and Info for Gear and Equippable
    gear_and_equippable_labels = f"{'Dmg':^{stats_space_w}}║{'Hp':^{stats_space_w}}║{'Str':^{stats_space_w}}║{'Agi':^{stats_space_w}}║{'Itn':^{stats_space_w}}║{'Def':^{stats_space_w}}║{'Spd':^{stats_space_w}}║"

    # Gear Table
    gear_top_parts =     f"╔{'═'*GEAR_SLOT}╦{'═'*GEAR_ITEM}╦{stat_info_top}"
    gear_middle_part =   f"╠{'═'*GEAR_SLOT}╬{'═'*GEAR_ITEM}╬{stat_info_middle}"
    gear_bottom_border = f"╚{'═'*GEAR_SLOT}╩{'═'*GEAR_ITEM}╩{stat_info_bottom}"

    # Equippable Table
    equippable_top_parts =     f"╔{'═'*equippable_slot_w}╦{stat_info_top}"
    equippable_middle_part =   f"╠{'═'*equippable_name_w}╬{stat_info_middle}"
    equippable_bottom_border = f"╚{'═'*equippable_name_w}╩{stat_info_bottom}"
    # add later
    # {'═'*equippable_index_w}═
    # {'═'*equippable_index_w}═
    # Titles Gear and Equippable
    gear_title_part =  f"║ {'Gear':^{gear_slot_name_w}} ║ {'Items':^{gear_item_name_w}} ║{gear_and_equippable_labels}"
    equippable_title_part =  f"║{'Equippable':^{equippable_slot_w}}║{gear_and_equippable_labels}"
    
    print(f"{left_side}{" " * (middle)}{right_side}")
    print(f"{left_side}{column_space_w}{gear_top_parts}{column_space_w}{equippable_top_parts}{column_space_w}{right_side}")
    print(f"{left_side}{column_space_w}{gear_title_part}{column_space_w}{equippable_title_part}{column_space_w}{right_side}")
    
    gear_lst = ["Head", "Chest", "Neck", "Legs", "Main-hand", "Off-hand"]
    equippable_lst = list(filter(lambda item : isinstance(item, Equippable), unit.backpack))

    for gear_slot_label, gear_slot, equippable_item in zip_longest(gear_lst, unit.gear.keys(), equippable_lst):
        # Unit Gear
        gear_obj = unit.gear.get(gear_slot) if gear_slot else None
        def get_gear_stat(name):
            if not gear_obj: 
                return "-"
            value = gear_obj.stats.get(name, 0)

            return value if value > 0 else "-"
        display_gear_label = gear_slot_label or " "

        gear_name = gear_obj.name if gear_obj else "---"
        get_gear_health = get_gear_stat("health")
        get_gear_strength = get_gear_stat("strength")
        get_gear_agility = get_gear_stat("agility")
        get_gear_intelligence = get_gear_stat("intelligence")
        get_gear_defence = get_gear_stat("defence")
        get_gear_speed = get_gear_stat("speed")

        if isinstance(gear_obj, Weapon):
            gear_weapon_damage = gear_obj.damage if gear_obj.damage > 0 else "-"
        else: 
            gear_weapon_damage = "-"
        
        def get_equippable_stat(name):
            if not equippable_item: 
                return "-"
            value = equippable_item.stats.get(name, 0)
            return value if value > 0 else "-"
        
        display_equippable_label = equippable_item.name if equippable_item else " "

        get_equippable_health_num = get_equippable_stat("health")
        get_equippable_strength_num = get_equippable_stat("strength")
        get_equippable_agility_num = get_equippable_stat("agility")
        get_equippable_intelligence_num = get_equippable_stat("intelligence")
        get_equippable_defence_num = get_equippable_stat("defence")
        get_equippable_speed_num = get_equippable_stat("speed")

        if isinstance(equippable_item, Weapon):
            equippable_weapon_damage = equippable_item.damage if equippable_item.damage > 0 else "-"
        else: 
            equippable_weapon_damage = "-"

        # Gear Table
        gear_stats_columns_txt = (
                                f"{gear_name:<{gear_item_name_w}} ║{gear_weapon_damage:^{stats_space_w}}║"
                                f"{get_gear_health:^{stats_space_w}}║{get_gear_strength:^{stats_space_w}}║"
                                f"{get_gear_agility:^{stats_space_w}}║{get_gear_intelligence:^{stats_space_w}}║"
                                f"{get_gear_defence:^{stats_space_w}}║{get_gear_speed:^{stats_space_w}}║")
        
        gear_table_into_txt =   f"║ {display_gear_label:<{gear_slot_name_w}} ║ {gear_stats_columns_txt}"

        # Equippable
        equippable_stats_columns = (
                                    f"{equippable_weapon_damage:^{stats_space_w}}║{get_equippable_health_num:^{stats_space_w}}║"
                                    f"{get_equippable_strength_num:^{stats_space_w}}║{get_equippable_agility_num:^{stats_space_w}}║"
                                    f"{get_equippable_intelligence_num:^{stats_space_w}}║{get_equippable_defence_num:^{stats_space_w}}║"
                                    f"{get_equippable_speed_num:^{stats_space_w}}║"
                                    )
        
        equippable_table_into =   f"║ {display_equippable_label:<{equippable_slot_name_w}} ║{equippable_stats_columns}"
    
       
        # Middle Part
        print(f"{left_side}{column_space_w}{gear_middle_part}{column_space_w}{equippable_middle_part}{column_space_w}{right_side}")
     
        # Bottom Part
        print(f"{left_side}{column_space_w}{gear_table_into_txt}{column_space_w}{equippable_table_into}{column_space_w}{right_side}")
    print(f"{left_side}{column_space_w}{gear_bottom_border}{column_space_w}{equippable_bottom_border}{column_space_w}{right_side}")

print(len("   1  "))