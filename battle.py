import time, random
from item_list import item_list, weapon_dict
from enemies import Enemy, enemies
from player import Player
from items import Item, Potion, Weapon
from constance import BOX_WIDTH

def get_health_print(player, enemy):
   player_hp = player.get_health_status()
   enemy_hp = enemy.get_health_status()
   print(f"Player HP: {player_hp}, Enemy HP: {enemy_hp}")

def take_a_rest(player):
   player.health += 5
   print(player.health)
   return player.health

def player_combat_choice(player, enemy):
   turn_in_progress = True
   while turn_in_progress:
 
       player_choice = input("1. Attack\n2. Use Potion\n")
       if player_choice == "1":
               enemy.receive_attack(player)
               turn_in_progress = False
       elif player_choice == "2":
               player.use_potion()

def print_result_of_combat(enemy):
   print(f"Z" * BOX_WIDTH)
   print(f"{player.name} defeated {enemy.name}!")
   print(f"Gaining {enemy.experience} exp!")
   print(f"Status:\nHealth: {player.health}, level: {player.level}, ATK: {player.attack}, DEF: {player.defence}, SPD: {player.speed}")
   print(f"Z" * BOX_WIDTH)

print("==========Welcome==========")
user_name = input("What is your name? ")
player = Player(user_name, health=5,power=3,defence=2,speed=2,level=1,experience=0)
print(f"=======Nice to meet you, {user_name}!=========")
menu = True
while menu:
    # options show_player_gear_and_inventory(), show_stats(), equip()
    print(f"1. Check Stats 2. Check Gear and Inventory 3. Equip 4.Depart")
    player_option = input("What will I do?")
    if player_option == "1":
        player.show_stats()
    elif player_option == "2":
        player.show_player_gear_and_inventory()
    elif player_option == "3":
        player.equip()
    elif player_option == "4":
        answer = input("Reade to explore the world?: ")
        lower_case_answer = answer.lower()
        if lower_case_answer == "yes":
            menu = False

for enemy in enemies:
    print("X" * BOX_WIDTH)
    print(f"A wild {enemy.name} (HP: {enemy.health}) is blocking your path!")
    print("X" * BOX_WIDTH)
    while player.status == "Alive" and enemy.status == "Alive":
        if player.speed > enemy.speed:
            order = [player, enemy]
        else:
            order = [enemy, player]

        for attacker in order:
            if attacker == player:
                # attack
                player_combat_choice(player, enemy)
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
        get_health_print(player, enemy)
        # If enemy die. Player should get exp, loot and possible gold
        if enemy.status == "Dead":
            print(f"{enemy.name} has fallen!")
            print_result_of_combat(enemy)
            # Player getting Exp
            player.gain_experience(enemy)
            # checking if the player has enough exp to lvl up
            player.level_up()
            #  What to do after a fight!
            after_a_fight = True
            while True:
                player_decision = input("Do you want to to rest or continue?\n1: Check Stats 2: Show Gear and Inventory 3: Equip 4: Rest 5.Continue\nYour choise is: ")
                if player_decision == "1":
                    player.show_stats()
                elif player_decision == "2":
                    player.show_player_gear_and_inventory()
                elif player_decision == "3":
                    player.equip()
                elif player_decision == "4":
                    take_a_rest(player)
                    after_a_fight = False
                else:
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







