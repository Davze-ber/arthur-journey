import time, ui, actions, enemies
from constance import BOX_WIDTH, BUTTON_WIDTH
from player import Player
from enemies import Enemy
 
from typing import Type
class Counter:
    def __init__(self):
        self.turn = 0
    def increment_turn(self):
        self.turn += 1
        return self.turn

def combat_beginnig(player, allies, enemy):
   # Player and allies team
   player_team = [player] + (allies if allies else [])
   player_team_size = len(player_team)

   # Enemy team/ Solo or multiple
   if isinstance(enemy, list):
      enemy_team =  enemy
   else:
      enemy_team = [enemy]
   return player_team, player_team_size, enemy_team

def combat_fighting(player, player_team, enemy_team):
   gold_loot = 0
   item_loot = []
   unit_order = sorted((player_team + enemy_team), key = lambda unit: unit.speed, reverse=True)

   combat_in_progress = True
   while combat_in_progress:
      if len(player_team) > 0 and len(enemy_team) > 0:
         combat_in_progress = False
         return combat_in_progress

      for unit in unit_order:
         for player_unit in player_team:
            for enemy_unit in enemy_team:
               print(f" {player_unit.name} HP: {player_unit.current_health}  -  {enemy_unit.name} HP: {enemy_unit.current_health}")
         if isinstance(unit, Player):
            if unit.status == "Dead":
               continue
            if unit.status == "Alive":
               targets = player_combat_choice(player, enemy_team)
               for target in targets:
                  if targets.status == "Dead":
                     enemy_team.remove(target)
                     print(f"{target.name} has fallen!")
                  
                     target_gold = target.gold if target.gold else 0
                     gold_loot += target_gold

                     target_loot = target.loot if target.loot else []
                     item_loot.append(target_loot)
               return gold_loot, item_loot
         # elif isinstance(unit, Ally):
         #    pass

         elif isinstance(unit, Enemy):
            if unit.status == "Alive":
               targets = player_combat_choice(player_team, enemy_team)
               for target in targets:
                  if targets.status == "Dead":
                     player_team.remove(target)
                     print(f"{target.name} has fallen!")


def combat_result(player, player_team,player_team_size, enemy_team, gold_loot, item_loot):
   if not player_team and len(enemy_team) >= 1:
      if player_team_size == 1:
         print(f"{player.name} was defeated!")
      else:
         print(f"Hero's party was defeated!")
   if len(player_team) >= 1 and not enemy_team:
      player.gold += gold_loot
      player.inventory.append(item_loot)
      print(f"Enemies were defeated!")

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
      unit_order = sorted((player_team + enemy_team), key = lambda unit: unit.speed, reverse=True)
      for player_unit in player_team:
         print(f" {player_unit.name} HP: {player_unit.current_health}")
               
      for enemy_unit in enemy_team:
         print(f"{enemy_unit.name} HP: {enemy_unit.current_health}")

      for unit in unit_order:
         if not player_team or not enemy_team:
            break

         if isinstance(unit, Player):
            if unit.status == "Dead":
               continue
            if unit.status == "Alive":
               targets = player_combat_choice(player, player_team, enemy_team)
               for target in targets:
                  if target.status == "Dead":
                     enemy_team.remove(target)
                     print(f"{target.name} has fallen!")

                     total_exp += target.experience
                  
                     target_gold = target.gold if hasattr(target, "gold") else 0
                     gold_loot += target_gold

                     target_loot = target.loot if target.loot else []
                     item_loot.extend(target_loot)
               
      

         elif isinstance(unit, Enemy):
            if unit.status == "Alive":
               targets = unit.choose_the_target(player_team, enemy_team)
               for target in targets:
                  if target.status == "Dead":
                     player_team.remove(target)
                     print(f"{target.name} has fallen!")

      
   if len(player_team) >= 1 and len(enemy_team) == 0:
      player.gain_experience(total_exp)
      player.gold += gold_loot
      player.inventory.extend(item_loot)
      print(f"Enemies were defeated!")
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


