
from entities.enemies import enemies_dict
from entities.playerCharacter import Player
import entities.playerCharacter as playerCharacter
from items_inventory.items import Item, Potion, Weapon
from ui_constance import BOX_WIDTH, BUTTON_WIDTH
import entities.playerActions as aP
import combatMechanics
import ui_components.ui_frames as ui_frames

def vocation_selector(vocation_choice):
    vocation = ""
    if vocation_choice == "1":
        vocation = "warrior"
    elif vocation_choice == "2":
        vocation = "ranger"
    elif vocation_choice == "3":
        vocation = "mage"
    return vocation

ui_frames.print_top_layer()
ui_frames.print_titles("Welcome!")
ui_frames.print_titles("Nice to meet you, Arthur!")
ui_frames.print_titles("Are you ready to go on the adventure?")
player = Player(name="Arthur", resource_type= None,vocation=None, health=5,strength=1,agility=1, intelligence=1, defense=1,speed=1,level=1,experience=0)
print("1. Warrior 2. Ranger 3. Mage")
ui_frames.print_bot_layer()
vocation_choice = input(">")
selected = vocation_selector(vocation_choice)
player.choose_vocation(selected)
# Player Stats
ui_frames.print_top_layer()
aP.show_menu(player)










 