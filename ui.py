from constance import BOX_WIDTH, BUTTON_WIDTH
 

left_top_corner = "/"
left_bot_corner = "\\"
right_top_corner = "\\"
right_bot_corner = "/"
border_char = "_"
border_width = BOX_WIDTH - 2
middle = BOX_WIDTH - 4
left_side = "| "
right_side = " |"

def print_top_layer():
    print(" " + (border_width * border_char) + " ")
    print(left_top_corner + (border_width * " ") + right_top_corner)

def print_bot_layer():
    print(left_bot_corner+ border_width * border_char + right_bot_corner)

def print_titles(title):
    return left_side + title.center(BOX_WIDTH-4) + right_side




def print_button(text):
    leght_text = len(text)
    count_space = BUTTON_WIDTH - len(left_side + right_side + text)
    
    return left_side + text.center(count_space) + right_side
   
# def print_line_with_buttons(*args):
#     button_texts = []
#     for button in args:
#         buttons = print_button(button)
#     total = len(args)
#     length_arg = sum(len(button) for button in args)
#     space_bewteen_buttons = BOX_WIDTH - 4 - length_arg / total
#     print_space =  " " * space_bewteen_buttons
#     return left_side + print_space + args



# def print_gear_and_inv(player):
#     player_gear = player.gear
#     player_inv = player.inventory


#     left_side +  ""

#  name, max_health, power, defence, speed, level, experience)
def show_player_stats(player):
        stat_name_length = 11
        gear_name_lenght = 12
        place_holder = 15
        head_name = player.gear["head"].name if player.gear["head"] else "Empty"
        chest_name = player.gear["chest"].name if player.gear["chest"] else "Empty"
        legs_name = player.gear["legs"].name if player.gear["legs"] else "Empty"
        main_name = player.gear["main_hand"].name if player.gear["main_hand"] else "Empty"
        off_name = player.gear["off_hand"].name if player.gear["off_hand"] else "Empty"

        health_head_line = f"|| {'Health':<{stat_name_length}}: {player.max_health:<3} || {'Head':<{gear_name_lenght}}: {head_name:<{place_holder}} ||"
        attack_chest_line =f"|| {'Attack':<{stat_name_length}}: {player.attack:<3} || {'Chest':<{gear_name_lenght}}: {chest_name:<{place_holder}} ||"
        defence_legs_line = f"|| {'Defence':<{stat_name_length}}: {player.defence:<3} || {'Legs':<{gear_name_lenght}}: {legs_name:<{place_holder}} ||"
        speed_main_hand_line = f"|| {'Speed':<{stat_name_length}}: {player.speed:<3} || {'Main-hand':<{gear_name_lenght}}: {main_name:<{place_holder}} ||"
        level_off_hand_line = f"|| {'Level':<{stat_name_length}}: {player.level:<3} || {'Off-hand':<{gear_name_lenght}}: {off_name:<{place_holder}} ||"
        experience_line = f"|| {'Experience':<{stat_name_length}}: {player.experience:<3} ||"

   
        # Var 1
        # print(left_side + "=" * middle + right_side)
        # print(f"{left_side}{health_head_line:<{middle}}{right_side}")
        # print(f"{left_side}{attack_chest_line:<{middle}}{right_side}")
        # print(f"{left_side}{defence_legs_line:<{middle}}{right_side}")
        # print(f"{left_side}{speed_main_hand_line:<{middle}}{right_side}")
        # print(f"{left_side}{level_off_hand_line:<{middle}}{right_side}")
        # print(f"{left_side}{experience_line:<{middle}}{right_side}")
        # print(left_side + "=" * middle + right_side)       
    
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
                
                
