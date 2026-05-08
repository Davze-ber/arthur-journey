from constance import BOX_WIDTH, BUTTON_WIDTH


left_top_corner = "/"
left_bot_corner = "\\"
right_top_corner = "\\"
right_bot_corner = "/"
middle_char = "_"
middle = BOX_WIDTH - len(left_top_corner) - len(right_top_corner)
left_side = "| "
right_side = " |"
def print_top_layer():
    print(" " + middle * middle_char + " ")
    print(left_top_corner+ middle * " " + right_top_corner)
def print_bot_layer():
    print(left_top_corner+ middle * " " + right_top_corner)
    print(" " + middle * middle_char + " ")
def print_titles(title):
    length_title = len(title)
    return left_side + title.center(BOX_WIDTH-4) + right_side




def print_button(text):
    leght_text = len(text)
    count_space = BUTTON_WIDTH - len(left_side + right_side + text)
    print_space = " " * count_space
    return left_side + text + print_space + right_side
   
# def print_line_with_buttons(*args):
#     button_texts = []
#     for button in args:
#         buttons = print_button(button)
#     total = len(args)
#     length_arg = sum(len(button) for button in args)
#     space_bewteen_buttons = BOX_WIDTH - 4 - length_arg / total
#     print_space =  " " * space_bewteen_buttons
#     return left_side + print_space + args
print(len("| 2. Check Gear and Inventory |"))


def print_gear_and_inv(player):
    player_gear = player.gear
    player_inv = player.inventory


    left_side +  ""

