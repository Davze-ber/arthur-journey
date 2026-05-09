from constance import BOX_WIDTH, BUTTON_WIDTH


def player_combat_choice(player, enemy):
   turn_in_progress = True
   while turn_in_progress:
 
       player_choice = input("1. Attack\n2. Use Potion\n")
       if player_choice == "1":
               enemy.receive_attack(player)
               turn_in_progress = False
       elif player_choice == "2":
               player.use_potion()


def print_result_of_combat(player, enemy):
   print(f"Z" * BOX_WIDTH)
   print(f"{player.name} defeated {enemy.name}!")
   print(f"Gaining {enemy.experience} exp!")
   print(f"Status:\nHealth: {player.current_health}/{player.max_health}, level: {player.level}, ATK: {player.attack}, DEF: {player.defence}, SPD: {player.speed}")
   print(f"Z" * BOX_WIDTH)

def get_health_print(player, enemy):
   player_hp = player.get_health_status()
   
   enemy_hp = enemy.get_health_status()
   print(f"Player HP: {player_hp}, Enemy HP: {enemy_hp}")



