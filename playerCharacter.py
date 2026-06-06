from character import Character
from items import Item, Weapon, Armor
from itemsDict import item_lst,weapon_dict
from spells import FireBolt
from typing import Any

import ui_components.ui_combat as ui_combat

class Player(Character):
    def __init__(self, name: str, resource_type: str, health: int, strength: int, agility: int, intelligence: int, defense: int, speed: int, level: int, experience: int):
        super().__init__(name, resource_type, health, strength, agility, intelligence, defense, speed, level, experience )
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
            item_lst["Lesser Potion"](),
            item_lst["Strong Potion"](),
            weapon_dict["Wood Stick"](),
            weapon_dict["Axe"]()
            ]

        
        self.spellbook = [
            FireBolt()
        ]

    def choose_the_target(self,player_team, enemy_team):
        if len(enemy_team) == 1:
            target = enemy_team[0]
        else:
            while True:
                for index, enemy in enumerate(enemy_team, start=1):
                    e_name_txt, e_hp_txt, e_hp_bar, e_res_txt, e_res_bar = ui_combat.format_unit_info(enemy)
                    print(f"{index}. {e_name_txt} {e_hp_txt} {e_hp_bar}{e_res_txt} {e_res_bar}", end=" ")
                print()
                choice = int(input("Which enemy to attack: "))-1
                target = (enemy_team[choice])
                break
        return target

    def take_a_rest(self, at_inn=False):
        percentage = 1 if at_inn else 0.5
        rest_healing = round(self.max_health * percentage)
        if self.current_health + rest_healing <= self.max_health:
            self.current_health += rest_healing
        else:
            self.current_health = self.max_health
        print(f"{self.name} recovered {rest_healing} health")

    def level_up(self):
        match self.experience:
            case exp if exp >= 30:
                self.level  = 4
                self.max_health += 5
                self.current_health +=5
                self.power += 4
                self.defense += 2
                self.speed += 1

            case exp if exp >= 15:
                self.level = 3
                self.max_health += 5
                self.current_health +=5
                self.power += 1
                self.defense += 2
                self.speed += 3

            case exp if exp >= 5:
                self.level =2
                self.max_health += 5
                self.current_health +=5
                self.power += 2
                self.defense += 1
                self.speed += 2
                
        return self.level,self.max_health, self.power,self.defense, self.speed



