from playerCharacter import Player
from character import Character
from enemies import Enemy, enemies_dict
from maps import world_map
from typing import Type
from items import Material, Junk

import playerActions
import ui_components.ui_combat as ui_combat

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
   total_gold = 0
   item_loot = []

   while len(player_team) > 0 and len(enemy_team) > 0:
      unit_order = sorted((player_team + enemy_team), key = lambda unit: unit.total_stats["speed"], reverse=True)

      ui_combat.combat_show_units_hp_resources(player_team, enemy_team)

      for unit in unit_order:
         if not unit.is_alive:
            if unit in player_team: player_team.remove(unit)
            if unit in enemy_team:
               enemy_team.remove(unit)

               total_exp += unit.experience
               total_gold += getattr(unit, "gold", 0)
               enemy_loot = getattr(unit, "loot", [])
               check_stackable_enemy(enemy_loot, item_loot)
               print(f"{unit.name} has fallen!")

            if check_teams_if_empty(player_team, enemy_team):
               break
            continue
      
         if unit.is_stunned:
            print(f"{unit.name} is stunned!")
            unit.is_stunned = False
            continue

         if isinstance(unit, Player):
            targets = player_combat_choice(player, player_team, enemy_team)
                 
         elif isinstance(unit, Enemy):
            targets = unit.choose_the_target(player_team, enemy_team)
         
         if check_teams_if_empty(player_team, enemy_team):
            break
     

         for target in targets:
            if not target.is_alive:
               print(f"{target.name} has been defeated!")
   
      
   if len(player_team) >= 1 and len(enemy_team) == 0:
      print(f"Enemies were defeated!")
      combat_loot_phase(player, player_team, total_exp, total_gold, item_loot)
      return "Victory"
   return "Defeat"
      
def combat_loot_phase(player, player_team, total_exp, total_gold, item_loot):
   party_members = len(player_team)
   exp_per_member = total_exp // party_members
   amount_of_loot = len(item_loot)

   for member in player_team:
      member.gain_experience(exp_per_member)

   player.inventory["gold"] += total_gold
   check_stackable_player(item_loot, player)

   print(f"All members gained {exp_per_member} EXP.")
   print(f"Party obtained {total_gold} and found {amount_of_loot}")
   for item in item_loot:
      print(f"{item.name} Amount: {item.amount} Value: {item.total_value}")
         
def player_combat_choice(player, player_team, enemy_team):
   turn_in_progress = True
   targets = []
   ui_combat.show_player_combat_option(player)

   while turn_in_progress:
      player_choice = input(">")
      if player_choice == "1":
         target = player.choose_the_target(player_team, enemy_team)
         player.basic_attack(target)
         targets = [target]
         turn_in_progress = False

      elif player_choice =="2":
         ui_combat.show_spells(player)
         choose_spell = int(input(">"))-1
         chosen_spell = player.spellbook[choose_spell]
         
         if chosen_spell.can_cast(player):
            target = player.choose_the_target(player_team, enemy_team)
            chosen_spell.deal_damage(player,target)
            chosen_spell.apply_cost(player)
            targets = [target]
            turn_in_progress = False
            
         else:
            print("I need more mana to cast")
            ui_combat.show_player_combat_option(player)
      elif player_choice == "3":
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


def stack_items_in_list(loot, target_list):
   for item in loot:
      if item.can_stack and item in target_list:
         item_index = target_list.index(item)
         target_list[item_index].amount += item.amount
      else:        
         target_list.append(item.clone())

def check_stackable_player(loot, player):
   
      stack_items_in_list(loot, player.inventory["backpack"])

def check_stackable_enemy(enemy_loot, item_loot):
   
      stack_items_in_list(enemy_loot, item_loot)