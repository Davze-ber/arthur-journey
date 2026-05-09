import time, random, ui
import actions, combat
from item_list import item_list, weapon_dict
from enemies import Enemy, enemies
from player import Player
from items import Item, Potion, Weapon
from constance import BOX_WIDTH, BUTTON_WIDTH


ui.print_top_layer()
print(ui.print_titles("Welcome!"))
print(ui.print_titles("Nice to meet you, Arthur!"))
print(ui.print_titles("Are you ready to go on the adventure?"))


# Player Stats
player = Player(name="Arthur", max_health=5,power=3,defence=2,speed=2,level=1,experience=0)

actions.show_menu(player)


for enemy in enemies:
    print("X" * BOX_WIDTH)
    print(f"A wild {enemy.name} (HP: {enemy.max_health}) is blocking your path!")
    print("X" * BOX_WIDTH)
    while player.status == "Alive" and enemy.status == "Alive":
        if player.speed > enemy.speed:
            order = [player, enemy]
        else:
            order = [enemy, player]


        for attacker in order:
            if attacker == player:
                # attack
                combat.player_combat_choice(player, enemy)
                # print health
                time.sleep(1)
                # check if still is allive
                if enemy.status == "Dead":
                    break
            else:
                # attack
                player.receive_attack(attacker)
                # check if still is allive
                time.sleep(1)
                if player.status == "Dead":
                    break
        # Print Health of player and enemy
        combat.get_health_print(player, enemy)
        # If enemy die. Player should get exp, loot and possible gold
        if enemy.status == "Dead":
            print(f"{enemy.name} has fallen!")
            combat.print_result_of_combat(player, enemy)
            # Player getting Exp
            player.gain_experience(enemy)
            # checking if the player has enough exp to lvl up
            player.level_up()
            #  What to do after a fight!
            after_a_fight = True
            while after_a_fight:
                player_decision = input("Do you want to to rest or continue?\n1: Check Stats 2: Show Gear and Inventory 3: Equip 4: Rest 5.Continue\nYour choise is: ")
                if player_decision == "1":
                    ui.show_player_stats(player)
                elif player_decision == "2":
                    player.show_player_gear_and_inventory()
                elif player_decision == "3":
                    player.equip()
                elif player_decision == "4":
                    actions.take_a_rest(player)
                    after_a_fight = False
                elif player_decision == "5":
                    after_a_fight = False
             
# If player die
if player.status == "Dead":
   print("X" * BOX_WIDTH)
   print(f"{enemy.name} defeated {player.name}! And the story of {player.name} ends")
   print("X" * BOX_WIDTH)        
#  If player beat the last enemy
if player.status == "Alive":
   print("X" * BOX_WIDTH)
   print(f"{player.name} has survive the long journey!")
   print("X" * BOX_WIDTH)


ui.print_bot_layer()














