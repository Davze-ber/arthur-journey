from ui_constance import BOX_WIDTH
from .ui_frames import left_side,right_side,col_w, middle, bot_border_char,top_border_char
def show_available_locations(world_map):
    MAP_INDEX = 5
    MAP_NAME = 10
    MAP_NAME_BORDER = 12
    MAP_LEVEL = 7

    map_top_part = f"╔{'═'*MAP_INDEX}╦{'═'*MAP_NAME_BORDER}╦{'═'*MAP_LEVEL}╗{' ' * 104}{col_w}{right_side}"
    map_mid_part = f"╠{'═'*MAP_INDEX}╬{'═'*MAP_NAME}╬{'═'*MAP_LEVEL}╣{' ' * 104}{col_w}{right_side}"
    map_bot_part = f"╚{'═'*MAP_INDEX}╩{'═'*MAP_NAME_BORDER}╩{'═'*MAP_LEVEL}╝{' ' * 104}{col_w}{right_side}"
    print(f"{left_side}{"World Map":^{middle}}{right_side}")
    print(f"{left_side}{col_w}{map_top_part}")
    for i, map, in enumerate(world_map.keys(), start=1):
        map_name = map
        map_recommended_level = world_map[map]["recommended_level"]

        print(f"{left_side}{col_w}║{i:^{MAP_INDEX}}║ {map_name.capitalize():<{MAP_NAME}} ║{map_recommended_level:^{MAP_LEVEL}}║{' ' * 104}{col_w}{right_side}")
        
        if len(world_map) > 1:
            print(f"{left_side}{col_w}{map_mid_part}")

    print(f"{left_side}{col_w}{map_bot_part}")
    print(f"{bot_border_char * BOX_WIDTH}")