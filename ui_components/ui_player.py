from ui_constance import BOX_WIDTH, BUTTON_WIDTH, COLUMN_SPACE
from ui_constance import STATS_NAME, STATS_SPACE, COMBAT_NAME, COMBAT_SPACE, NAME_SPACE, GEAR_ITEM, GEAR_SLOT, EQUIPPABLE_NAME #Stats, Combat, Gear, Equippable
from itertools import zip_longest
from items import Armor, Weapon, Potion, Equippable, Item, Junk, Material
from .ui_frames import left_side,right_side, middle, print_empty_line
from .ui_combat import format_unit_info
# Stats and Combat Widths
stat_name_w = STATS_NAME
stats_space_w = STATS_SPACE

combat_name_w = COMBAT_NAME
combat_space_w = COMBAT_SPACE
combat_space_long_w = COMBAT_SPACE +1
combat_stats_space_w = STATS_SPACE+1
column_space_w = COLUMN_SPACE * " "

# middle_long_space_w = DESCRIPTION_NAME +2
# column_space_longer_w = (COLUMN_SPACE +1) * " "


gear_slot_w = GEAR_SLOT
gear_slot_name_w = gear_slot_w - 1
gear_item_name_w = GEAR_ITEM - 1

gear_lst = ["Head", "Neck", "Chest", "Legs", "Main-hand", "Off-hand"]

def get_stat(obj, name):
    if not obj: 
        return "-"
    value = obj.stats.get(name, 0)
    return value if value > 0 else "-"

def get_stats_table(unit):
    rows = []
    rows.append( f"╔{'═'*stat_name_w}╦{'═'*stat_name_w}╗")
    rows.append(f"║ {'Attributes':^{NAME_SPACE}} ║ {'Total':^{NAME_SPACE}} ║")
    for stat_name in unit.core_stats.keys():
        # Stats
        total_values = unit.total_stats.get(stat_name, 0)
        core_values = unit.core_stats.get(stat_name, 0)
        bonus_values = unit.bonus_stats.get(stat_name, 0)

        rows.append(f"╠{'═'*stat_name_w}╬{'═'*stat_name_w}╣")
        rows.append(f"║ {stat_name.capitalize():<{NAME_SPACE}} ║ {total_values:^{stats_space_w}}({core_values:^{stats_space_w}}+{bonus_values:^{stats_space_w}}) ║")

    rows.append(f"╚{'═'*stat_name_w}╩{'═'*stat_name_w}╝")
    return rows
    
def get_combat_stats_table(unit):
    rows = []
    rows.append( f"╔{'═'*combat_name_w}╦{'═'*combat_space_long_w}╗")
    rows.append(f"║ {'Combat':^{NAME_SPACE}} ║{'Total':^{NAME_SPACE+5}}║")
    for combat_stat_name in unit.combat_stats.keys():
        # Stats
        total_combat_values = unit.total_combat_stats.get(combat_stat_name, 0)
        combat_values = unit.combat_stats.get(combat_stat_name, 0)
        bonus_combat_values = unit.bonus_combat_stats.get(combat_stat_name, 0)

        rows.append(f"╠{'═'*combat_name_w}╬{'═'*combat_space_long_w}╣")
        rows.append(f"║ {combat_stat_name.capitalize():<{NAME_SPACE}} ║ {"{:.0f}".format(total_combat_values):^{combat_stats_space_w}}({"{:.0f}".format(combat_values):^{combat_stats_space_w}}+{"{:.0f}".format(bonus_combat_values):^{combat_stats_space_w}}) ║")

    rows.append(f"╚{'═'*combat_name_w}╩{'═'*combat_space_long_w}╝")
    return rows

def get_gear_table(unit):
    rows = []

    rows.append(f"╔{'═'*GEAR_SLOT}╦{'═'*GEAR_ITEM}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╗")
    rows.append(f"║{'Slot':^{GEAR_SLOT}}║{'Item':^{GEAR_ITEM}}║{'WP':^{stats_space_w}}║{'SP':^{stats_space_w}}║{'Hp':^{stats_space_w}}║{'Str':^{stats_space_w}}║{'Agi':^{stats_space_w}}║{'Itn':^{stats_space_w}}║{'Def':^{stats_space_w}}║{'Spd':^{stats_space_w}}║")
    

    for gear_slot_label, gear_slot in zip_longest(gear_lst, unit.gear.keys()):
        # Unit Gear
        gear_obj = unit.gear.get(gear_slot) if gear_slot else None

        display_gear_label = gear_slot_label or " "

        gear_name = gear_obj.name if gear_obj else "---"
        get_gear_health = get_stat(gear_obj,"health")
        get_gear_strength = get_stat(gear_obj,"strength")
        get_gear_agility = get_stat(gear_obj,"agility")
        get_gear_intelligence = get_stat(gear_obj,"intelligence")
        get_gear_defense = get_stat(gear_obj,"defense")
        get_gear_speed = get_stat(gear_obj,"speed")

        if isinstance(gear_obj, Weapon):
            gear_weapon_damage = gear_obj.weapon_damage if gear_obj.weapon_damage > 0 else "-"
            gear_spell_power = gear_obj.spell_power if gear_obj.spell_power > 0 else "-"
        else: 
            gear_weapon_damage = "-"
            gear_spell_power = "-"

        gear_stats_columns_txt = (
                        f"║ {display_gear_label:<{gear_slot_name_w}}║{gear_name:<{gear_item_name_w}} ║{gear_weapon_damage:^{stats_space_w}}║{gear_spell_power:^{stats_space_w}}║"
                        f"{get_gear_health:^{stats_space_w}}║{get_gear_strength:^{stats_space_w}}║"
                        f"{get_gear_agility:^{stats_space_w}}║{get_gear_intelligence:^{stats_space_w}}║"
                        f"{get_gear_defense:^{stats_space_w}}║{get_gear_speed:^{stats_space_w}}║")
        rows.append(f"╠{'═'*GEAR_SLOT}╬{'═'*GEAR_ITEM}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╣")
        rows.append(gear_stats_columns_txt)
    rows.append(f"╚{'═'*GEAR_SLOT}╩{'═'*GEAR_ITEM}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╝")
    return rows
# def get_buff_debuff_table(unit,status):
#     if status == "buff":
        
#     rows = []
#     rows.append( f"╔{'═'*stats_space_w}╦{'═'*middle_long_space_w}╦{'═'*7}╗")
#     rows.append(f"║ {buff_name:<{NAME_SPACE}}║ {buff_descriptions:<{DESCRIPTION_SPACE}} ║ {buff_duration:^{TURN_SPACE}} ║")
#     for buff_debuff in unit.core_stats.keys():
#         # Stats
#         total_values = unit.total_stats.get(stat_name, 0)
#         core_values = unit.core_stats.get(stat_name, 0)
#         bonus_values = unit.bonus_stats.get(stat_name, 0)

#         rows.append(f"╠{'═'*stats_space_w}╬{'═'*middle_long_space_w}╬{'═'*7}╣")
#         rows.append(f"║ {stat_name.capitalize():<{NAME_SPACE}}║ {total_values:^{stats_space_w}}({core_values:^{stats_space_w}}+{bonus_values:^{stats_space_w}}) ║")

#     rows.append(f"╚{'═'*stats_space_w}╩{'═'*middle_long_space_w}╩{'═'*7}╝")
#     return rows


# top_part_long =    f"╔{'═'*stats_space_w}╦{'═'*middle_long_space_w}╦{'═'*7}╗"
#     middle_part_long = f"╠{'═'*stats_space_w}╬{'═'*middle_long_space_w}╬{'═'*7}╣"
#     bot_part_long =    f"╚{'═'*stats_space_w}╩{'═'*middle_long_space_w}╩{'═'*7}╝"

#     # Titles Attibutes Buffs Debuffs
#     stats_title_part =  f"║ {'Attributes':^{title_space_w}} ║ {'Total':^{title_space_w}} ║"
#     buffs_title_part =  f"║ {'Buffs':^{title_space_w}} ║ {'Description':^{DESCRIPTION_SPACE}} ║ {'Turns':^5} ║"
#     debufs_title_part = f"║ {'Debuffs':^{title_space_w}} ║ {'Description':^{DESCRIPTION_SPACE}} ║ {'Turns':^5} ║"

def print_stats_table(unit):
    unit_stats = get_stats_table(unit)
    unit_combat = get_combat_stats_table(unit)
    unit_gear = get_gear_table(unit)
    unit_name_txt, unit_hp_txt, unit_hp_bar, unit_res_txt, unit_res_bar = format_unit_info(unit)
    print_empty_line()
    unit_info =f"{unit.name:<10}{column_space_w}Level: {unit.level:<3}{column_space_w}Experience: {unit.experience:<6}{column_space_w}Gold: {unit.gold:<6}{unit_hp_txt}{unit_hp_bar}{unit_res_txt}{unit_res_bar}"

    print(f"{left_side}{column_space_w}{unit_info}{column_space_w}{right_side}")
    print_empty_line()
    for gear_item, stats, combat_stats in zip_longest(unit_gear, unit_stats, unit_combat):
        print(f"{left_side}{column_space_w}{stats}{column_space_w}{combat_stats}{column_space_w}{gear_item}{column_space_w}{right_side}")

    