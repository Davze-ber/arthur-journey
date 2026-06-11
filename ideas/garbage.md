  def receive_attack(self, opponent):
        incoming_damage = opponent.attack + random.randint(-2,+2)
        damage = max(0, incoming_damage - self.total_stats[defence])
        self.current_health -= damage
        print(f"{self.name} took {damage} damage!")
        if self.current_health <= 0:
            self.current_health = 0
            self.status = "Dead"

#  name, max_health, power, defence, speed, level, experience)
def show_unit_stats(unit):
        stat_name_length = 11
        gear_name_lenght = 12
        place_holder = 15
        head_name = unit.gear["head"].name if unit.gear["head"] else "Empty"
        chest_name = unit.gear["chest"].name if unit.gear["chest"] else "Empty"
        legs_name = unit.gear["legs"].name if unit.gear["legs"] else "Empty"
        main_name = unit.gear["main_hand"].name if unit.gear["main_hand"] else "Empty"
        off_name = unit.gear["off_hand"].name if unit.gear["off_hand"] else "Empty"

        health_head_line = f"|| {'Health':<{stat_name_length}}: {unit.max_health:<3} || {'Head':<{gear_name_lenght}}: {head_name:<{place_holder}} ||"
        attack_chest_line =f"|| {'Attack':<{stat_name_length}}: {unit.attack:<3} || {'Chest':<{gear_name_lenght}}: {chest_name:<{place_holder}} ||"
        defence_legs_line = f"|| {'Defence':<{stat_name_length}}: {unit.defence:<3} || {'Legs':<{gear_name_lenght}}: {legs_name:<{place_holder}} ||"
        speed_main_hand_line = f"|| {'Speed':<{stat_name_length}}: {unit.speed:<3} || {'Main-hand':<{gear_name_lenght}}: {main_name:<{place_holder}} ||"
        level_off_hand_line = f"|| {'Level':<{stat_name_length}}: {unit.level:<3} || {'Off-hand':<{gear_name_lenght}}: {off_name:<{place_holder}} ||"
        experience_line = f"|| {'Experience':<{stat_name_length}}: {unit.experience:<3} ||"

        #  Var 2
        print_top_layer()
        print(left_side + "=" * middle + right_side)
        print(f"{left_side}{health_head_line:<{middle}}{right_side}")
        print(f"{left_side}{attack_chest_line:<{middle}}{right_side}")
        print(f"{left_side}{defence_legs_line:<{middle}}{right_side}")
        print(f"{left_side}{speed_main_hand_line:<{middle}}{right_side}")
        print(f"{left_side}{level_off_hand_line:<{middle}}{right_side}")
        print(f"{left_side}{experience_line:<{middle}}{right_side}")
        print(left_side + "=" * middle + right_side) 
        print_bot_layer()  

equippable = list(filter(lambda item : isinstance(item, (Armor, Weapon), unit.inventory["backpack"])))

# def show_unit_stats_buffs_debuffs(unit):
#     stats_space_w = MIDDLE_SPACE
#     middle_long_space_w = DESCRIPTION_NAME +2
#     stats_space_w = STATS_SPACE
#     title_space_w = TITLE_SPACE
#     column_space_w = COLUMN_SPACE * " "
#     column_space_longer_w = (COLUMN_SPACE +1) * " "

#     # Borders
#     top_part =    f"╔{'═'*stats_space_w}╦{'═'*stats_space_w}╗"
#     middle_part = f"╠{'═'*stats_space_w}╬{'═'*stats_space_w}╣"
#     bot_part =    f"╚{'═'*stats_space_w}╩{'═'*stats_space_w}╝"
#     top_part_long =    f"╔{'═'*stats_space_w}╦{'═'*middle_long_space_w}╦{'═'*7}╗"
#     middle_part_long = f"╠{'═'*stats_space_w}╬{'═'*middle_long_space_w}╬{'═'*7}╣"
#     bot_part_long =    f"╚{'═'*stats_space_w}╩{'═'*middle_long_space_w}╩{'═'*7}╝"

#     # Titles Attibutes Buffs Debuffs
#     stats_title_part =  f"║ {'Attributes':^{title_space_w}} ║ {'Total':^{title_space_w}} ║"
#     buffs_title_part =  f"║ {'Buffs':^{title_space_w}} ║ {'Description':^{DESCRIPTION_SPACE}} ║ {'Turns':^5} ║"
#     debufs_title_part = f"║ {'Debuffs':^{title_space_w}} ║ {'Description':^{DESCRIPTION_SPACE}} ║ {'Turns':^5} ║"

#     print(f"{left_side}{" " * (middle)}{right_side}")
#     print(f"{left_side}{column_space_w}{top_part}{column_space_w}{top_part_long}{column_space_longer_w}{top_part_long}{column_space_w}{right_side}")
#     print(f"{left_side}{column_space_w}{stats_title_part}{column_space_w}{buffs_title_part}{column_space_longer_w}{debufs_title_part}{column_space_w}{right_side}")
    
#     for stat_name, buff_obj, debuff_obj in zip_longest(unit.core_stats, unit.buff_lst, unit.debuff_lst):
#         # Stats
#         total_values = unit.total_stats.get(stat_name, 0)
#         core_values = unit.core_stats.get(stat_name, 0)
#         bonus_values = unit.bonus_stats.get(stat_name, 0)
#         # Buffs
#         if buff_obj:
#             buff_name = buff_obj.name.capitalize()
#             buff_descriptions = buff_obj.description
#             buff_duration = buff_obj.duration
#         else:
#             buff_name = "---"
#             buff_descriptions = "---"
#             buff_duration = "---"

#         # Debufss
#         if buff_obj:
#             debuff_name = debuff_obj.name.capitalize()
#             debuff_descriptions = debuff_obj.description
#             debuff_duration = debuff_obj.duration
#         else:
#             debuff_name = "---"
#             debuff_descriptions = "---"
#             debuff_duration = "---"
            
#         # Middle Part
#         stats_part =   f"║ {stat_name.capitalize():<{NAME_SPACE}}║ {total_values:^{stats_space_w}}({core_values:^{stats_space_w}}+{bonus_values:^{stats_space_w}}) ║"
#         buffs_part =   f"║ {buff_name:<{NAME_SPACE}}║ {buff_descriptions:<{DESCRIPTION_SPACE}} ║ {buff_duration:^{TURN_SPACE}} ║"
#         debuffs_part = f"║ {debuff_name:<{NAME_SPACE}}║ {debuff_descriptions:<{DESCRIPTION_SPACE}} ║ {debuff_duration:^{TURN_SPACE}} ║"
#         print(f"{left_side}{column_space_w}{middle_part}{column_space_w}{middle_part_long}{column_space_longer_w}{middle_part_long}{column_space_w}{right_side}")
#         print(f"{left_side}{column_space_w}{stats_part}{column_space_w}{buffs_part}{column_space_longer_w}{debuffs_part}{column_space_w}{right_side}")
#         # Bottom Part

#     print(f"{left_side}{column_space_w}{bot_part}{column_space_w}{bot_part_long}{column_space_longer_w}{bot_part_long}{column_space_w}{right_side}")

# def show_inventory(unit):
#     print(unit.gold)
#     equippable = [item for item in unit.inventory["backpack"] if isinstance(item, Equippable)]
#     potions = [potion for potion in unit.inventory["backpack"] if isinstance(potion, Potion)] 
#     others = [other for other in unit.inventory["backpack"] if isinstance(other, (Junk, Material))]
#     indexed_equippable = [(i, item) for i, item in enumerate(equippable, start=1)]
#     indexed_potions = [(i, potion) for i, potion in enumerate(potions, start=1)]
#     indexed_others = [(i, potion) for i, potion in enumerate(others, start=1)] 


#     for (item_i, item), (potion_i, potion,)  in zip_longest(indexed_equippable, indexed_potions, ):
#         print(f"{item_i} {item.name} {potion_i} {potion.name}")
        
#         potion_part = f"{potion_i}. {potion.name} {potion.healing_amount} {potion.restore_mana}" 


# def show_unit_gear_inv(unit, player_backpack): 
#     # Gear
#     gear_slot_w = GEAR_SLOT
#     gear_slot_name_w = gear_slot_w - 2
#     gear_item_name_w = GEAR_ITEM - 2
#     # Equippable
#     equippable_slot_w = EQUIPPABLE_NAME
#     equippable_slot_name_w = EQUIPPABLE_NAME - 2
#     equippable_index_w = 3
#     equippable_name_w = equippable_slot_w - 0
#     stats_space_w = STATS_SPACE +2 
#     column_space_w = COLUMN_SPACE * " "

#     # Info for Gear and Equippable
#     stat_info_top =    f"{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╦{'═'*stats_space_w}╗"
#     stat_info_middle = f"{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╬{'═'*stats_space_w}╣"
#     stat_info_bottom = f"{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╩{'═'*stats_space_w}╝"
#     # Labels and Info for Gear and Equippable
#     gear_and_equippable_labels = f"{'Dmg':^{stats_space_w}}║{'Hp':^{stats_space_w}}║{'Str':^{stats_space_w}}║{'Agi':^{stats_space_w}}║{'Itn':^{stats_space_w}}║{'Def':^{stats_space_w}}║{'Spd':^{stats_space_w}}║"

#     # Gear Table
#     gear_top_parts =     f"╔{'═'*GEAR_SLOT}╦{'═'*GEAR_ITEM}╦{stat_info_top}"
#     gear_middle_part =   f"╠{'═'*GEAR_SLOT}╬{'═'*GEAR_ITEM}╬{stat_info_middle}"
#     gear_bottom_border = f"╚{'═'*GEAR_SLOT}╩{'═'*GEAR_ITEM}╩{stat_info_bottom}"

#     # Equippable Table
#     equippable_top_parts =     f"╔{'═'*equippable_slot_w}╦{stat_info_top}"
#     equippable_middle_part =   f"╠{'═'*equippable_name_w}╬{stat_info_middle}"
#     equippable_bottom_border = f"╚{'═'*equippable_name_w}╩{stat_info_bottom}"
#     # add later
#     # {'═'*equippable_index_w}═
#     # {'═'*equippable_index_w}═
#     # Titles Gear and Equippable
#     gear_title_part =  f"║ {'Gear':^{gear_slot_name_w}} ║ {'Items':^{gear_item_name_w}} ║{gear_and_equippable_labels}"
#     equippable_title_part =  f"║{'Equippable':^{equippable_slot_w}}║{gear_and_equippable_labels}"
    
#     print(f"{left_side}{" " * (middle)}{right_side}")
#     print(f"{left_side}{column_space_w}{gear_top_parts}{column_space_w}{equippable_top_parts}{column_space_w}{right_side}")
#     print(f"{left_side}{column_space_w}{gear_title_part}{column_space_w}{equippable_title_part}{column_space_w}{right_side}")
    

#     equippable_lst = list(filter(lambda item : isinstance(item, Equippable), player_backpack.backpack))

#     for gear_slot_label, gear_slot, equippable_item in zip_longest(gear_lst, unit.gear.keys(), equippable_lst):
#         # Unit Gear
#         gear_obj = unit.gear.get(gear_slot) if gear_slot else None

#         display_gear_label = gear_slot_label or " "

#         gear_name = gear_obj.name if gear_obj else "---"
#         get_gear_health = get_stat(gear_obj,"health")
#         get_gear_strength = get_stat(gear_obj,"strength")
#         get_gear_agility = get_stat(gear_obj,"agility")
#         get_gear_intelligence = get_stat(gear_obj,"intelligence")
#         get_gear_defense = get_stat(gear_obj,"defense")
#         get_gear_speed = get_stat(gear_obj,"speed")

#         if isinstance(gear_obj, Weapon):
#             gear_weapon_damage = gear_obj.weapon_damage if gear_obj.weapon_damage > 0 else "-"
#         else: 
#             gear_weapon_damage = "-"
        
#         display_equippable_label = equippable_item.name if equippable_item else " "

#         get_equippable_health_num = get_stat(equippable_item,"health")
#         get_equippable_strength_num = get_stat(equippable_item,"strength")
#         get_equippable_agility_num = get_stat(equippable_item,"agility")
#         get_equippable_intelligence_num = get_stat(equippable_item,"intelligence")
#         get_equippable_defense_num = get_stat(equippable_item,"defense")
#         get_equippable_speed_num = get_stat(equippable_item,"speed")

#         if isinstance(equippable_item, Weapon):
#             equippable_weapon_damage = equippable_item.weapon_damage if equippable_item.weapon_damage > 0 else "-"
#         else: 
#             equippable_weapon_damage = "-"

#         # Gear Table
#         gear_stats_columns_txt = (
#                                 f"{gear_name:<{gear_item_name_w}} ║{gear_weapon_damage:^{stats_space_w}}║"
#                                 f"{get_gear_health:^{stats_space_w}}║{get_gear_strength:^{stats_space_w}}║"
#                                 f"{get_gear_agility:^{stats_space_w}}║{get_gear_intelligence:^{stats_space_w}}║"
#                                 f"{get_gear_defense:^{stats_space_w}}║{get_gear_speed:^{stats_space_w}}║")
        
#         gear_table_into_txt =   f"║ {display_gear_label:<{gear_slot_name_w}} ║ {gear_stats_columns_txt}"

#         # Equippable
#         equippable_stats_columns = (
#                                     f"{equippable_weapon_damage:^{stats_space_w}}║{get_equippable_health_num:^{stats_space_w}}║"
#                                     f"{get_equippable_strength_num:^{stats_space_w}}║{get_equippable_agility_num:^{stats_space_w}}║"
#                                     f"{get_equippable_intelligence_num:^{stats_space_w}}║{get_equippable_defense_num:^{stats_space_w}}║"
#                                     f"{get_equippable_speed_num:^{stats_space_w}}║"
#                                     )
        
#         equippable_table_into =   f"║ {display_equippable_label:<{equippable_slot_name_w}} ║{equippable_stats_columns}"
    
       
#         # Middle Part
#         print(f"{left_side}{column_space_w}{gear_middle_part}{column_space_w}{equippable_middle_part}{column_space_w}{right_side}")
     
#         # Bottom Part
#         print(f"{left_side}{column_space_w}{gear_table_into_txt}{column_space_w}{equippable_table_into}{column_space_w}{right_side}")
#     print(f"{left_side}{column_space_w}{gear_bottom_border}{column_space_w}{equippable_bottom_border}{column_space_w}{right_side}")






