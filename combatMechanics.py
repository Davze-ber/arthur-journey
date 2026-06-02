import time, visuals, playerActions
from constance import BOX_WIDTH, BUTTON_WIDTH
from playerCharacter import Player
from enemies import Enemy, enemies_dict
from maps import plains, world_map
from typing import Type

class Counter:
    def __init__(self):
        self.turn = 0
    def increment_turn(self):
        self.turn += 1
        return self.turn

def combat(player, allies, enemy):
   # Player and allies team
   player_team = [player] + (allies if allies else [])
   player_team_size = len(player_team)

   # Enemy team/ Solo or multiple
   if isinstance(enemy, list):
      enemy_team =  enemy
   else:
      enemy_team = [enemy]
      
   total_exp = 0
   gold_loot = 0
   item_loot = []

   while len(player_team) > 0 and len(enemy_team) > 0:
      unit_order = sorted((player_team + enemy_team), key = lambda unit: unit.total_stats["speed"], reverse=True)

      visuals.combat_show_units_hp_resources(player_team, enemy_team)

      for unit in unit_order:
         if check_teams_if_empty(player_team, enemy_team):
            break

         if unit.is_alive == False:
            if unit in player_team:
               player_team.remove(unit)

            if unit in enemy_team:
               enemy_team.remove(unit)

            if check_teams_if_empty(player_team, enemy_team):
               break
            
            continue

         if unit.is_stunned == True:
            print(f"{unit.name} is stunned!")
            unit.is_stunned = False
            continue

         if isinstance(unit, Player):
                  targets = player_combat_choice(player, player_team, enemy_team)
                  for target in targets:
                     if target.is_alive == False:
                        enemy_team.remove(target)
                        print(f"{target.name} has fallen!")

                        total_exp += target.experience
                     
                        target_gold = target.gold if hasattr(target, "gold") else 0
                        gold_loot += target_gold

                        target_loot = target.backpack if target.backpack else []
                        item_loot.extend(target_loot)
                        
                     if check_teams_if_empty(player_team, enemy_team):
                        break
                 
                     
         elif isinstance(unit, Enemy):
               targets = unit.choose_the_target(player_team, enemy_team)
               for target in targets:
                  if target.is_alive == False:
                     player_team.remove(target)
                     print(f"{target.name} has fallen!")
                     if check_teams_if_empty(player_team, enemy_team):
                        break
   

      
   if len(player_team) >= 1 and len(enemy_team) == 0:
      print(f"Enemies were defeated!")
      player.gain_experience(total_exp)
      player.inventory["gold"] += gold_loot
      player.backpack.extend(item_loot)
      return "Victory"
   return "Defeat"
      
         
def player_combat_choice(player, player_team, enemy_team):
   turn_in_progress = True
   targets = []
   while turn_in_progress:
      player_choice = input("1. Attack\n2. Use Potion\n")
      if player_choice == "1":
         targets = player.choose_the_target(player_team, enemy_team)
         turn_in_progress = False
      elif player_choice == "2":
               player.use_potion()
   return targets


def enter_the_map(player, allies, map):
   current_map = world_map[map]
   map_floors = current_map["floors"]
   map_name = current_map.get("name")
   print(f"Entering {map_name}")
   for current_floor in map_floors.values():
      floor_level = current_floor["level"]
      floor_enemies = current_floor["enemies"]
      floor_is_done = current_floor["is_done"]
   
     
      print(f"Floor: {floor_level}")
      
      current_enemies = [enemies_dict[enemy]() for enemy in floor_enemies]

      result = combat(player, allies, current_enemies)
      
      if result == "Victory":
         current_floor["is_done"] = True
         playerActions.after_a_fight(player)
      elif result == "Defeat":
         print("You are wounded! You must retreat!")
         player.take_a_rest(at_inn=True)
         player.is_alive = True
         break


def check_teams_if_empty(player_team, enemy_team):
   if not player_team or not enemy_team:
      return True