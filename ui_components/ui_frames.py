from ui_constance import BOX_WIDTH, BUTTON_WIDTH, COLUMN_SPACE
from ui_constance import COMBAT_HP_RES_BAR, COMBAT_HP_RES_LEN, COMBAT_HP_RES_SPACE, COMBAT_NAME_SPACE
import re
top_border_char = "▄"
bot_border_char = "▀"
border_width = BOX_WIDTH - 2
middle = BOX_WIDTH - 4
left_side = "█ "
right_side = " █"
column_space_w = COLUMN_SPACE * " "
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
    print(f"{left_side}{title:^{middle}}{right_side}")

def print_two_titles(map_name, floor_level):
    map_floor = f"Entering: {map_name} Floor: {floor_level}"
    print(f"{left_side}{map_floor:^{middle}}{right_side}")

def print_button(text):
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
 