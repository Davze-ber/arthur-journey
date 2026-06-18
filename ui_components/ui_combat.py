from ui_constance import COMBAT_HP_RES_BAR, COMBAT_HP_RES_LEN, COMBAT_HP_RES_SPACE, COMBAT_NAME_SPACE
from itertools import zip_longest
from .ui_frames import left_side,right_side, col_w

def show_hp_and_res_bar(unit):
    if not unit:
        return (" " * COMBAT_HP_RES_BAR, " " * COMBAT_HP_RES_BAR)
    display_char = "■"
        # Health
    unit_percentage_health = (unit.current_health / unit.max_health) * 100
    multiply_hp = int(unit_percentage_health // 20)
    unit_health_bar = display_char * multiply_hp
    # Resource4
    unit_percentage_res = (unit.current_resource / unit.max_resource) * 100
    multiply_res = int( unit_percentage_res // 20)
    unit_res_bar = display_char * multiply_res

    return (unit_health_bar, unit_res_bar)

def format_unit_info(unit):
    if not unit:
        return (" " * COMBAT_NAME_SPACE,
                " " * COMBAT_HP_RES_SPACE,
                " " * COMBAT_HP_RES_BAR,
                " " * COMBAT_HP_RES_SPACE,
                " " * COMBAT_HP_RES_BAR
                )

    unit_hp_bar, unit_res_bar = show_hp_and_res_bar(unit)

    # Unit Helth info
    unit_hp_txt =  f"HP: {unit.current_health}"
    display_hp_bar = f"[{unit_hp_bar:<{COMBAT_HP_RES_LEN}}] "    
    # unit_hp_txt_v2 =  f"HP: {unit.current_health}/{unit.max_health}"

    # Unit Res info
    unit_res_txt = f"{unit.resource_type.capitalize()}: {unit.current_resource}"
    display_res_bar = f"[{unit_res_bar:<{COMBAT_HP_RES_LEN}}]"    
    # unit_res_txt_v2 = f"{unit.resource_type.capitalize()}: {unit.current_resource}/{unit.max_resource}"
    return (unit.name, unit_hp_txt, display_hp_bar, unit_res_txt, display_res_bar)

def combat_show_units_hp_resources(player_team, enemy_team):
    for player_unit, enemy_unit in zip_longest(player_team, enemy_team):
        # Player Info
        p_name_txt, p_hp_txt, p_hp_bar, p_res_txt, p_res_bar = format_unit_info(player_unit)
        player_party_info = f"{p_name_txt:<{COMBAT_NAME_SPACE}}{p_hp_txt:<{COMBAT_HP_RES_SPACE}}{p_hp_bar:<{COMBAT_HP_RES_BAR}}{p_res_txt:<{COMBAT_HP_RES_SPACE}}{p_res_bar:<{COMBAT_HP_RES_BAR}}"
                            
        # Enemy Info
        e_name_txt, e_hp_txt, e_hp_bar, e_res_txt, e_res_bar = format_unit_info(enemy_unit)
        enemy_party_info = f"{e_name_txt:<{COMBAT_NAME_SPACE}}{e_hp_txt:<{COMBAT_HP_RES_SPACE}}{e_hp_bar:<{COMBAT_HP_RES_BAR}}{e_res_txt:<{COMBAT_HP_RES_SPACE}}{e_res_bar:<{COMBAT_HP_RES_BAR}}"
                            
        print(f"{left_side}{column_space_w}{player_party_info}{' ' * 48}{enemy_party_info}{column_space_w}{right_side}")

def show_player_combat_option(player):
    if player.resource_type in ["rage", "energy"]:
      player_option = f"1. Attack 2. Skills 3. Use Potion"
    elif player.resource_type == "mana":
      player_option = f"1. Attack 2. Spell Book 3. Use Potion"
    print(f"{left_side}{column_space_w}{player_option:<133}{column_space_w}{right_side}")

def show_spells(unit):
    for i, spell in enumerate(unit.spellbook, start=1):
                spell_cost_damage = spell.display_cost_damage(unit)
                print(f"{i}. {spell.name}, {spell.category} {spell.tag}, {spell_cost_damage}")