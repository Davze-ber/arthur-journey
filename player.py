import random
from character import Character
from items import Item, Weapon, Armor
from item_list import item_list,weapon_dict
from constance import BOX_WIDTH

class Player(Character):
    def __init__(self, name, max_health, power, defence, speed, level, experience):
        super().__init__(name,max_health, power, defence, speed, level, experience)
      
        self.gear = {
           "head": None,
           "chest": None,
           "legs": None,
           "main_hand": None ,
           "off_hand":None,
                   }
        self.backpack_size = 2

        self.inventory = [item_list["Lesser Potion"](), item_list["Strong Potion"](),weapon_dict["Wood Stick"]()]


    @property
    def attack(self):
        total_attack = self.power + self.bonus_attack


        weapon = self.gear.get("main_hand")
        if weapon and hasattr(weapon, "damage"):
            total_attack += weapon.damage
        return total_attack
  
    def calc_attack(self):
        if hasattr(self.gear["main_weapon"],"damage"):
            return self.attack + Weapon.damage

    def equip(self):
        self.show_player_gear_and_inventory()
        gear_slot_item = None
        item_index = int(input("What item to equip?"))
        chosen_item = self.inventory[item_index-1]
        if isinstance(chosen_item, Weapon):
            if self.gear["main_hand"] == None:
                self.gear["main_hand"] = chosen_item
                self.inventory.remove(chosen_item)
            else:
                gear_slot_item = self.gear["main_hand"]
                self.gear["main_hand"] = chosen_item
                self.inventory.remove(chosen_item)
                self.inventory.append(gear_slot_item)
        elif isinstance(chosen_item, Armor):
            if self.gear["main_hand"] == None:
                self.gear["main_hand"] = chosen_item
                self.inventory.remove(chosen_item)
            else:
                gear_slot_item = self.gear["main_hand"]
                self.gear["main_hand"] = chosen_item
                self.inventory.remove(chosen_item)
                self.inventory.append(gear_slot_item)        

    def show_player_gear_and_inventory(self):
        head_name = self.gear["head"].name if self.gear["head"] else "Empty"
        chest_name = self.gear["chest"].name if self.gear["chest"] else "Empty"
        legs_name = self.gear["legs"].name if self.gear["legs"] else "Empty"
        main_name = self.gear["main_hand"].name if self.gear["main_hand"] else "Empty"
        off_name = self.gear["off_hand"].name if self.gear["off_hand"] else "Empty"

        gear_lines = f"Head: {head_name}\nChest: {chest_name}\nLegs: {legs_name}\nMain-Hand: {main_name}\nOff-Hand: {off_name}"
        print(gear_lines)
        # lines = [item.strip() for item in gear_lines.split(",")]
        # self.draw_box(BOX_WIDTH, lines)
        for index, item in  enumerate(self.inventory):
            print(f"{index + 1}: {item.name}")

    def show_stats(self):
        print(f"Level: {self.level}, Exp: {self.experience}, Health: {self.max_health}, Attack: {self.attack}, Defence: {self.defence}, Speed: {self.speed}")


    def draw_box(width, lines):
        inner_width = width - 6  # "X " + " X"

        print("=" * width)

        for line in lines:
            padding = inner_width - len(line)
            print("|| " + line + " " * padding + " ||")

        print("=" * width)



    def gain_experience(self, target):
        self.experience += target.experience
        return self.experience




    def level_up(self):
        match self.experience:
            case exp if exp >= 30:
               self.level  = 4
               self.health += 5
               self.power += 4
               self.defence += 2
               self.speed += 1




            case exp if exp >= 15:
               self.level = 3
               self.health += 5
               self.power += 1
               self.defence += 2
               self.speed += 3




            case exp if exp >= 5:
               self.level =2
               self.health += 5
               self.power += 2
               self.defence += 1
               self.speed += 2
             
        return self.level,self.health, self.power,self.defence, self.speed









