import random, visuals
from character import Character
from items import Item, Weapon, Armor
from itemsDict import item_list,weapon_dict
from constance import BOX_WIDTH
from spells import FireBolt

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
            item_list["Lesser Potion"](),
            item_list["Strong Potion"](),
            weapon_dict["Wood Stick"](),
            weapon_dict["Axe"]()
            ]

        
        self.spellbook = [
            FireBolt()
        ]
    
    
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

            for i, spell in enumerate(self.spellbook):
                spell_name = spell.name
                spell_description = spell.description
                spell_cost_damage = spell.display_cost_damage(self)
                print(i, spell_name,spell_description, spell_cost_damage)

            spell_index = int(input("Choose Spell: ")) -1
            chosen_spell = self.spellbook[spell_index]
            if chosen_spell.can_cast(self):
                choose_target = int(input("choose target:")) -1
                chosen_enemy = enemy_team[choose_target]
                target = chosen_spell.deal_damage(self, chosen_enemy)
                spell.apply_cost(self)
                return [chosen_enemy]
        else:
    
            while True:
                try:
                    for index, enemy in enumerate(enemy_team):

                        e_name_txt, e_hp_txt, e_hp_bar, e_res_txt, e_res_bar = visuals.format_unit_info(enemy)
                        print(f"{index + 1}. {e_name_txt} {e_hp_txt} {e_hp_bar}{e_res_txt} {e_res_bar}", end=" ")
                    print()
                    choice = int(input("Which enemy to attack: "))
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



