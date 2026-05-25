  def receive_attack(self, opponent):
        incoming_damage = opponent.attack + random.randint(-2,+2)
        damage = max(0, incoming_damage - self.total_stats[defence])
        self.current_health -= damage
        print(f"{self.name} took {damage} damage!")
        if self.current_health <= 0:
            self.current_health = 0
            self.status = "Dead"

#  name, max_health, power, defence, speed, level, experience)
def show_unit_stats(unit):
        stat_name_length = 11
        gear_name_lenght = 12
        place_holder = 15
        head_name = unit.gear["head"].name if unit.gear["head"] else "Empty"
        chest_name = unit.gear["chest"].name if unit.gear["chest"] else "Empty"
        legs_name = unit.gear["legs"].name if unit.gear["legs"] else "Empty"
        main_name = unit.gear["main_hand"].name if unit.gear["main_hand"] else "Empty"
        off_name = unit.gear["off_hand"].name if unit.gear["off_hand"] else "Empty"

        health_head_line = f"|| {'Health':<{stat_name_length}}: {unit.max_health:<3} || {'Head':<{gear_name_lenght}}: {head_name:<{place_holder}} ||"
        attack_chest_line =f"|| {'Attack':<{stat_name_length}}: {unit.attack:<3} || {'Chest':<{gear_name_lenght}}: {chest_name:<{place_holder}} ||"
        defence_legs_line = f"|| {'Defence':<{stat_name_length}}: {unit.defence:<3} || {'Legs':<{gear_name_lenght}}: {legs_name:<{place_holder}} ||"
        speed_main_hand_line = f"|| {'Speed':<{stat_name_length}}: {unit.speed:<3} || {'Main-hand':<{gear_name_lenght}}: {main_name:<{place_holder}} ||"
        level_off_hand_line = f"|| {'Level':<{stat_name_length}}: {unit.level:<3} || {'Off-hand':<{gear_name_lenght}}: {off_name:<{place_holder}} ||"
        experience_line = f"|| {'Experience':<{stat_name_length}}: {unit.experience:<3} ||"

        #  Var 2
        print_top_layer()
        print(left_side + "=" * middle + right_side)
        print(f"{left_side}{health_head_line:<{middle}}{right_side}")
        print(f"{left_side}{attack_chest_line:<{middle}}{right_side}")
        print(f"{left_side}{defence_legs_line:<{middle}}{right_side}")
        print(f"{left_side}{speed_main_hand_line:<{middle}}{right_side}")
        print(f"{left_side}{level_off_hand_line:<{middle}}{right_side}")
        print(f"{left_side}{experience_line:<{middle}}{right_side}")
        print(left_side + "=" * middle + right_side) 
        print_bot_layer()  

equippable = list(filter(lambda item : isinstance(item, (Armor, Weapon), unit.inventory["backpack"])))