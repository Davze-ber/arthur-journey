from constance import BOX_WIDTH, BUTTON_WIDTH
 
top_border_char = "▄"
bot_border_char = "▀"
border_width = BOX_WIDTH - 2
middle = BOX_WIDTH - 4
left_side = "█ "
right_side = " █"

def print_top_layer():
    print(f"{top_border_char*BOX_WIDTH}")
    print(left_side + (middle * " ") + right_side)

def print_bot_layer():
    print(f"{bot_border_char*BOX_WIDTH}")

def print_titles(title):
    return left_side + title.center(BOX_WIDTH-4) + right_side




def print_button(text):
    leght_text = len(text)
    count_space = BUTTON_WIDTH - len(left_side + right_side + text)
    print(f"{top_border_char*15}",end="")
    print(f"{left_side}{text:^11}{right_side}", end="")
    print(f"{bot_border_char*15}", end="")
    
def print_menu(text1,text2,text3,text4):
    space = " " *3
    width_button = 22
    middle_button = 18
    print(f"{left_side}{top_border_char*width_button}{space}{top_border_char*width_button}{space}{top_border_char*width_button}{space}{top_border_char*width_button}{right_side}")
    print(f"{left_side}{left_side}{text1:^{middle_button}}{right_side}{space}{left_side}{text2:^{middle_button}}{right_side}{space}{left_side}{text3:^{middle_button}}{right_side}{space}{left_side}{text4:^{middle_button}}{right_side}{right_side}")
    print(f"{left_side}{bot_border_char*width_button}{space}{bot_border_char*width_button}{space}{bot_border_char*width_button}{space}{bot_border_char*width_button}{right_side}")
 
    

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
   
                
def print_row(unit):
    middle_space = 14
    stats_space = 3
    title_space = 12
    column_space = 3 * " "

    head_name = unit.gear["head"].name if unit.gear["head"] else "Empty"
    chest_name = unit.gear["chest"].name if unit.gear["chest"] else "Empty"
    legs_name = unit.gear["legs"].name if unit.gear["legs"] else "Empty"
    main_name = unit.gear["main_hand"].name if unit.gear["main_hand"] else "Empty"
    off_name = unit.gear["off_hand"].name if unit.gear["off_hand"] else "Empty"
    gear_lst = [head_name,chest_name,legs_name,main_name,off_name]

    print(f"{left_side}╔{"═"*middle_space}╦{"═"*middle_space}╗")
    print(f"{left_side}║ {"Attributes":^{title_space}} ║ {"Total":^{title_space}} ║")
    
    for stat_name, gear in zip(unit.core_stats, gear_lst):
        total_values = unit.total_stats.get(stat_name, 0)
        core_values = unit.core_stats.get(stat_name, 0)
        bonus_values = unit.bonus_stats.get(stat_name, 0)
        print(f"{left_side}╠{"═"*middle_space}╬{"═"*middle_space}╣")
        print(f"{left_side}║ {stat_name.capitalize():<13}║ {total_values:^{stats_space}}({core_values:^{stats_space}}+{bonus_values:^{stats_space}}) ║{column_space}║ {gear}")
    print(f"{left_side}╚{"═"*middle_space}╩{"═"*middle_space}╝")

"still need to update"