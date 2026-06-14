from ui_constance import BOX_WIDTH, BUTTON_WIDTH, COLUMN_SPACE
from ui_constance import STATS_NAME, STATS_SPACE, COMBAT_NAME, COMBAT_SPACE, NAME_SPACE
from ui_constance import GEAR_ITEM, GEAR_SLOT, EQUIPPABLE_NAME #Stats, Combat, Gear, Equippable
from ui_constance import BUFF_NAME, BUFF_DESCRIPTION, BUFF_EFFECT, BUFF_DURATION
from ui_constance import POTION_NAME, POTION_EFFECT, ITEM_VALUE
from ui_constance import OTHER_NAME, OTHER_AMOUNT
from itertools import zip_longest
from items_inventory.items import Armor, Weapon, Potion, Equippable, Item, Junk, Material
from .ui_frames import left_side,right_side, middle, print_empty_line
from .ui_combat import format_unit_info
# Stats and Combat Widths
stat_name_w = STATS_NAME
stats_w = STATS_SPACE

combat_name_w = COMBAT_NAME
combat_space_w = COMBAT_SPACE
combat_space_long_w = COMBAT_SPACE +1
combat_stats_w = STATS_SPACE+1

col_w = COLUMN_SPACE * " "
col_m_w = (COLUMN_SPACE+3) * " "
col_l_w = (COLUMN_SPACE+7) * " "

gear_slot_w = GEAR_SLOT
gear_slot_name_w = gear_slot_w - 1
gear_item_name_w = GEAR_ITEM - 1

gear_lst = ["Head", "Neck", "Chest", "Legs", "Main-hand", "Off-hand"]

def get_stat(obj, name):
    if not obj: 
        return "-"
    value = obj.stats.get(name, 0)
    return value if value > 0 else "-"

def get_value(obj, name):
    if not obj:
        return "-"
    value = getattr(obj, name, "-")
    return value

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
        rows.append(f"║ {stat_name.capitalize():<{NAME_SPACE}} ║ {total_values:^{stats_w}}({core_values:^{stats_w}}+{bonus_values:^{stats_w}}) ║")

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
        rows.append(f"║ {combat_stat_name.capitalize():<{NAME_SPACE}} ║ {"{:.0f}".format(total_combat_values):^{combat_stats_w}}({"{:.0f}".format(combat_values):^{combat_stats_w}}+{"{:.0f}".format(bonus_combat_values):^{combat_stats_w}}) ║")

    rows.append(f"╚{'═'*combat_name_w}╩{'═'*combat_space_long_w}╝")
    return rows

def get_gear_table(unit):
    rows = []

    rows.append(f"╔{'═'*GEAR_SLOT}╦{'═'*GEAR_ITEM}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╗")
    rows.append(f"║{'Slot':^{GEAR_SLOT}}║{'Item':^{GEAR_ITEM}}║{'WP':^{stats_w}}║{'SP':^{stats_w}}║{'Hp':^{stats_w}}║{'Str':^{stats_w}}║{'Agi':^{stats_w}}║{'Itn':^{stats_w}}║{'Def':^{stats_w}}║{'Spd':^{stats_w}}║")
    

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
                        f"║ {display_gear_label:<{gear_slot_name_w}}║{gear_name:<{gear_item_name_w}} ║{gear_weapon_damage:^{stats_w}}║{gear_spell_power:^{stats_w}}║"
                        f"{get_gear_health:^{stats_w}}║{get_gear_strength:^{stats_w}}║"
                        f"{get_gear_agility:^{stats_w}}║{get_gear_intelligence:^{stats_w}}║"
                        f"{get_gear_defense:^{stats_w}}║{get_gear_speed:^{stats_w}}║")
        rows.append(f"╠{'═'*GEAR_SLOT}╬{'═'*GEAR_ITEM}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╣")
        rows.append(gear_stats_columns_txt)
    rows.append(f"╚{'═'*GEAR_SLOT}╩{'═'*GEAR_ITEM}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╝")
    return rows

def get_equippable_table(unit, value=False):
    equippable_lst = list(filter(lambda item: isinstance(item, Equippable), unit.backpack))
    eq_name_b_w = EQUIPPABLE_NAME
    eq_name_w = eq_name_b_w -2
    val_text_w = ITEM_VALUE

    if value == True:
        val_title_w = f"║{'Val':^{val_text_w}}║"
        val_t_w =  f"╦{'═'*val_text_w}╗"
        val_m_w = f"╬{'═'*val_text_w}╣"
        val_b_w = f"╩{'═'*val_text_w}╝"
    else:
        val_title_w = f"║"
        val_t_w =  f"╗"
        val_m_w = f"╣"
        val_b_w = f"╝"


    rows = []
    rows.append(f"╔{'═'*(eq_name_b_w)}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}╦{'═'*stats_w}{val_t_w}")
    rows.append(f"║{'Equippable':^{eq_name_b_w}}║{'WP':^{stats_w}}║{'SP':^{stats_w}}║{'Hp':^{stats_w}}║{'Str':^{stats_w}}║{'Agi':^{stats_w}}║{'Itn':^{stats_w}}║{'Def':^{stats_w}}║{'Spd':^{stats_w}}{val_title_w}")

    for _, equip in zip_longest(range(6),equippable_lst):
        display_equippable_label = equip.name if equip else "-"

        eq_health_num = get_stat(equip,"health")
        eq_str_num = get_stat(equip,"strength")
        eq_agi_num = get_stat(equip,"agility")
        eq_int_num = get_stat(equip,"intelligence")
        eq_def_num = get_stat(equip,"defense")
        eq_spd_num = get_stat(equip,"speed")

        if isinstance(equip, Weapon):
            eq_wd = equip.weapon_damage if equip.weapon_damage > 0 else "-"
            eq_sp = equip.spell_power if equip.spell_power > 0 else "-"
        else: 
            eq_wd = "-"
            eq_sp = "-"

        if value == True:
            equip_value = equip.value if equip else "-"
            eq_val = f"║{equip_value:^{val_text_w}}║"
        else: 
            equip_value = ""
            eq_val = "║"
        gear_stats_columns_txt = (
                        f"║ {display_equippable_label:<{eq_name_w}} ║{eq_wd:^{stats_w}}║{eq_sp:^{stats_w}}║"
                        f"{eq_health_num:^{stats_w}}║{eq_str_num:^{stats_w}}║"
                        f"{eq_agi_num:^{stats_w}}║{eq_int_num:^{stats_w}}║"
                        f"{eq_def_num:^{stats_w}}║{eq_spd_num:^{stats_w}}{eq_val}")
        rows.append(f"╠{'═'* (eq_name_b_w)}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}╬{'═'*stats_w}{val_m_w}")
        rows.append(gear_stats_columns_txt)
    rows.append(f"╚{'═'* (eq_name_b_w)}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}╩{'═'*stats_w}{val_b_w}")
    return rows

def get_potions(unit):
    potions = list(filter(lambda item: isinstance(item, Potion), unit.backpack))
    w1, w2, w3 = POTION_NAME, POTION_EFFECT, ITEM_VALUE
    b1, b2 ,b3 = POTION_NAME-2, POTION_EFFECT-2, ITEM_VALUE

    rows = []

    rows.append(f"╔{'═'*w1}╦{'═'*w2}╦{'═'*w3}╗")
    rows.append(f"║{'Potion':^{w1}}║{'Effect':^{w2}}║{'Val':^{w3}}║")

    for _, potion in zip_longest(range(6), potions):

        p_name = get_value(potion, "name")
        p_name_short = p_name.replace("Potion", "")
        p_val = get_value(potion, "value")
        p_heal = get_value(potion, "healing_amount")
        p_mana = get_value(potion, "restore_mana")
        
        if potion:
            if potion.tag == "rejuvenation":
                restore_val = f"HP+ {p_heal:>3} MP+ {p_mana:>3}"
            elif potion.tag == "health":
                restore_val = f"HP+ {p_heal:>3}"
            elif potion.tag == "mana":
                restore_val = f"MP+ {p_mana:>3}"
        else:
            restore_val = "-"

        rows.append(f"╠{'═'*w1}╬{'═'*w2}╬{'═'*w3}╣")
        rows.append(f"║ {p_name_short:<{b1}} ║ {restore_val:<{b2}} ║{p_val:^{b3}}║")
    rows.append(f"╚{'═'*w1}╩{'═'*w2}╩{'═'*w3}╝")
    return rows

def get_other(unit):
    other_lst = list(filter(lambda item: isinstance(item, (Junk, Material)), unit.backpack))

    w1, w2, w3 = OTHER_NAME, OTHER_AMOUNT, ITEM_VALUE
    b1, b2 ,b3 = OTHER_NAME-2, OTHER_AMOUNT, ITEM_VALUE

    rows = []

    rows.append(f"╔{'═'*w1}╦{'═'*w2}╦{'═'*w3}╗")
    rows.append(f"║{'Item':^{w1}}║{'Amt':^{w2}}║{'Val':^{w3}}║")

    for _, item in zip_longest(range(6), other_lst):
        i_name = get_value(item, "name")
        i_amount = get_value(item, "amount")
        i_value = get_value(item, "total_value")

        rows.append(f"╠{'═'*w1}╬{'═'*w2}╬{'═'*w3}╣")
        rows.append(f"║ {i_name:<{b1}} ║{i_amount:^{b2}}║{i_value:^{b3}}║")
    rows.append(f"╚{'═'*w1}╩{'═'*w2}╩{'═'*w3}╝")
    return rows


def get_buff_debuff(unit, buffdebuff):
    b_n_b_w = BUFF_NAME
    b_n_w = b_n_b_w -2
    b_d_b_w = BUFF_DESCRIPTION
    b_des_w = b_d_b_w -2
    b_e_b_w = BUFF_EFFECT
    b_e_w = b_e_b_w -2
    b_dur_b_w = BUFF_DURATION
    b_dur_w = b_dur_b_w -2

    if buffdebuff == "buff":
        show_lst = unit.buff_lst
        title = "Buffs"
    elif buffdebuff == "debuff":
        show_lst = unit.debuff_lst
        title = "Debuffs"
    rows = []
    
    rows.append(f"╔{'═'*b_n_b_w}╦{'═'*b_d_b_w}╦{'═'*b_e_b_w}╦{'═'*b_dur_b_w}╗")
    rows.append(f"║ {title:^{b_n_w}} ║ {'Description':^{b_des_w}} ║ {'Effect':^{b_e_w}} ║ {'Duration':^{b_dur_w}} ║")
    for _, status in zip_longest(range(6),show_lst):
    
        s_name = status.name if status else "---"
        s_description = status.description if status else "---"
        s_effect = status.effect if status else "---"
        s_duration = status.duration if status else "---"

        rows.append(f"╠{'═'*b_n_b_w}╬{'═'*b_d_b_w}╬{'═'*b_e_b_w}╬{'═'*b_dur_b_w}╣")
        rows.append(f"║ {s_name:<{b_n_w}} ║ {s_description:<{b_des_w}} ║ {s_effect:<{b_e_w}} ║{s_duration:^{b_dur_b_w}}║")

    rows.append(f"╚{'═'*b_n_b_w}╩{'═'*b_d_b_w}╩{'═'*b_e_b_w}╩{'═'*b_dur_b_w}╝")
    return rows

def print_stats_table(unit):
    unit_stats = get_stats_table(unit)
    unit_combat = get_combat_stats_table(unit)
    unit_gear = get_gear_table(unit)
    unit_name_txt, unit_hp_txt, unit_hp_bar, unit_res_txt, unit_res_bar = format_unit_info(unit)
    print_empty_line()
    unit_info =f"{unit.name:<10}{col_w}Level: {unit.level:<3}{col_w}Experience: {unit.experience:<6}{col_w}Gold: {unit.gold:<6}{unit_hp_txt}{unit_hp_bar}{unit_res_txt}{unit_res_bar}"

    print(f"{left_side}{col_w}{unit_info}{col_w}{right_side}")
    print_empty_line()
    for gear_item, stats, combat_stats in zip_longest(unit_gear, unit_stats, unit_combat):
        print(f"{left_side}{col_w}{stats}{col_w}{combat_stats}{col_w}{gear_item}{col_w}{right_side}")

def print_gear_equippable(unit):
    unit_gear = get_gear_table(unit)
    unit_equippale = get_equippable_table(unit)
    print_empty_line()
    for gear, equip in zip_longest(unit_gear, unit_equippale):
        print(f"{left_side}{col_m_w}{gear}{col_l_w}{equip}{col_m_w}{right_side}")


def print_buffs_debuffs(unit):
    unit_buffs = get_buff_debuff(unit, "buff")
    unit_debuffs = get_buff_debuff(unit, "debuff")
    print_empty_line()
    for buff in unit_buffs:
        print(f"{left_side}{buff:^{middle}}{right_side}")
    for debuff in unit_debuffs:
        print(f"{left_side}{debuff:^{middle}}{right_side}")

def print_inventory(unit):
    unit_equippable = get_equippable_table(unit,value=True)
    unit_potions = get_potions(unit)
    unit_other = get_other(unit)

    print_empty_line()
    for equip, potion, other in zip(unit_potions, unit_equippable, unit_other):
        print(f"{left_side}{col_w}{equip}{col_w}{potion}{col_w}{other}{col_w}{right_side}")



def show_inventory(unit):
    equippable = [item for item in unit.inventory["backpack"] if isinstance(item, Equippable)]
    
    others = [other for other in unit.inventory["backpack"] if isinstance(other, (Junk, Material))]
    indexed_equippable = [(i+1, item) for i, item in enumerate(equippable)]
    
    indexed_others = [(i+1, potion) for i, potion in enumerate(others)] 
    for index, item in indexed_equippable:
        print(f"{index}. {item.name} Value: {item.value}")
        


    for index, other in indexed_others:
        print_empty_line()
        print(f"{index}. {other.name} Amount: {other.amount} Value: {other.total_value}")
    print(unit.gold)



