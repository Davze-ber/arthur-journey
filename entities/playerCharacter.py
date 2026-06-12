from entities.character import Character
from items import Item, Weapon, Armor
from itemsDict import item_lst, weapon_dict, shield_dict, armor_dict
from abilities.spells import FireBolt
from typing import Any
import abilities.spellbook as spellbook
import ui_components.ui_combat as ui_combat

class Player(Character):
    def __init__(self, name: str, resource_type: str,vocation: str, health: int, strength: int, agility: int, intelligence: int, defense: int, speed: int, level: int, experience: int):
        super().__init__(name, "None", health, strength, agility, intelligence, defense, speed, level, experience )
        self.vocation = vocation
        self.faction:str = "player"
        self.allies = []
        self.gear: dict[str,Any]= {
           "head": None,
           "chest": None,
           "neck" : None,
           "legs": None,
           "main_hand": None ,
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
     
        ]

        self.choose_vocation(vocation)

        if self.resource_type == "rage":
            self.current_resource = 0
        else:
            self.current_resource = self.max_resource

    def choose_vocation(self, job):
        if job == "warrior":
            self.vocation = "warrior"
            self.core_stats["strength"] += 1
            self.gear["main_hand"] = weapon_dict["Wood Stick"]()
            self.gear["off_hand"] = shield_dict["Small Shield"]()
            self.resource_type = "rage"
            self.current_resource = 0
        elif job == "ranger":
            self.vocation = "ranger"
            self.core_stats["agility"] += 1
            self.gear["main_hand"] = None
            self.resource_type = "energy"
            self.current_resource = self.max_resource
        elif job == "mage":
            self.vocation = "mage"
            self.core_stats["intelligence"] += 1
            self.gear["main_hand"] = weapon_dict["Wand"]()
            self.resource_type = "mana"
            self.current_resource = self.max_resource

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



