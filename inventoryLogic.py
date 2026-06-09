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