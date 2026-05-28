import random
from character import Character
from items import Item, Weapon, Armor
from itemsDict import item_list,weapon_dict
from constance import BOX_WIDTH

class Player(Character):
    def __init__(self, name: str, resource_type: str, health: int, strength: int, agility: int, intelligence: int, defence: int, speed: int, level: int, experience: int):
        super().__init__(name, resource_type, health, strength, agility, intelligence, defence, speed, level, experience )
        self.faction:str = "player"
        self.allies = []
        self.gear: dict[str,Any]= {
           "head": None,
           "chest": None,
           "neck" : None,
           "legs": None,
           "main_hand":  weapon_dict["Wood Stick"]() ,
           "off_hand":None,
                   }
        
        self.inventory["gold"] = 10
        self.inventory["backpack"] = [
            item_list["Lesser Potion"](),
            item_list["Strong Potion"](),
            weapon_dict["Wood Stick"](),
            weapon_dict["Axe"]()
            ]

        
    
    def equip(self):

        self.show_player_gear_and_inventory()
        gear_slot_item = None
        item_index = int(input("What item to equip?"))
        item_in_backpack = self.inventory["backpack"].index(item_index)
        chosen_item = self.backpack[item_in_backpack]

        if isinstance(chosen_item, Weapon):
            if self.gear["main_hand"] == None:
                self.gear["main_hand"] = chosen_item
                self.backpack.pop(item_index-1)
            else:
                gear_slot_item = self.gear["main_hand"]
                self.gear["main_hand"] = chosen_item
                self.backpack.pop(item_index-1)
                self.backpack.append(gear_slot_item)
        elif isinstance(chosen_item, Armor):
            if self.gear["main_hand"] == None:
                self.gear["main_hand"] = chosen_item
                self.backpack.pop(chosen_item)
            else:
                gear_slot_item = self.gear["main_hand"]
                self.gear["main_hand"] = chosen_item
                self.backpack.pop(item_index-1)
                self.backpack.append(gear_slot_item)        

    def show_player_gear_and_inventory(self):
        head_name = self.gear["head"].name if self.gear["head"] else "Empty"
        chest_name = self.gear["chest"].name if self.gear["chest"] else "Empty"
        legs_name = self.gear["legs"].name if self.gear["legs"] else "Empty"
        main_name = self.gear["main_hand"].name if self.gear["main_hand"] else "Empty"
        off_name = self.gear["off_hand"].name if self.gear["off_hand"] else "Empty"

        gear_lines = f"Head: {head_name}\nChest: {chest_name}\nLegs: {legs_name}\nMain-Hand: {main_name}\nOff-Hand: {off_name}"
        print(gear_lines)
        equipable_items = list(filter (lambda item: isinstance(item, (Weapon,Armor)), self.backpack))
        for index, item in  enumerate(equipable_items):
            print(f"{index + 1}: {item.name}")
        print("X: Exit")

    def choose_the_target(self,player_team, enemy_team):
        if len(enemy_team) == 1:
            target = enemy_team[0]
            self.basic_attack(target)
            return [target]
        else:
            while True:
                try:
                    for index, enemy in enumerate(enemy_team):
                        print(f"{index + 1}. {enemy.name} HP: {enemy.current_health}/{enemy.max_health}")
                    choice = int(input("Which enemy to attack"))
                    target = (enemy_team[choice - 1])
                    break
                except(ValueError, IndexError):
                    print("Invalid choice! Pick a number from the list")
            self.basic_attack(target)
            return [target]


    def take_a_rest(self, at_inn=False):
        percentage = 1 if at_inn else 0.5
        rest_healing = round(self.max_health * percentage)
        if self.current_health + rest_healing <= self.max_health:
            self.current_health += rest_healing
        else:
            self.current_health = self.max_health
        print(f"{self.name} recovered {rest_healing} health")

    def gain_experience(self, total_exp):
        self.experience += total_exp
        return self.experience

    def level_up(self):
        match self.experience:
            case exp if exp >= 30:
                self.level  = 4
                self.max_health += 5
                self.current_health +=5
                self.power += 4
                self.defence += 2
                self.speed += 1

            case exp if exp >= 15:
                self.level = 3
                self.max_health += 5
                self.current_health +=5
                self.power += 1
                self.defence += 2
                self.speed += 3

            case exp if exp >= 5:
                self.level =2
                self.max_health += 5
                self.current_health +=5
                self.power += 2
                self.defence += 1
                self.speed += 2
                
        return self.level,self.max_health, self.power,self.defence, self.speed










