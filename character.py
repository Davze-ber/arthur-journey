import random
from items import Item, Weapon, Potion


class Character:
    def __init__(self, name, max_health, power, defence, speed, level, experience):
        # Core Stats
        self.name = name
        self.current_health = max_health
        self.max_health = max_health
        self.power = power
        self.defence = defence
        self.speed = speed
        self.faction = None
        # Bonus Stats
        self.bonus_attack = 0
        self.bonus_defence = 0
        # Level Stats
        self.level = level
        self.experience = experience
        # Status
        self.status = "Alive"
        # Gear and Inventory
        self.gear = {
            "head": None,
            "chest": None,
            "legs": None,
            "main_hand": None,
            "off_hand":None,
                    }
        self.inventory = []
        self.buff_lst = []
        self.debuff_lst = []
        self.can_take_action = True    


    @property
    def attack(self):
        return self.power + self.bonus_attack


    def choose_the_target(self,player_team, enemy_team):
        if self.faction == "player" or  self.faction == "ally":
            target = enemy_team[0]
          
        elif self.faction == "enemy":
            target = player_team[0]

        self.basic_attack(target)
        return [target]


    def basic_attack(self, target):
        incoming_damage = self.attack + random.randint(-2,+2)
        damage_taken = max(0, incoming_damage - target.defence)
        target.current_health -= damage_taken
        print(f"{self.name} dealt {damage_taken} damage to {target.name}!")
        if target.current_health <= 0:
            target.current_health = 0
            target.status = "Dead"

    def receive_attack(self, opponent):
        incoming_damage = opponent.attack + random.randint(-2,+2)
        damage = max(0, incoming_damage - self.defence)
        self.current_health -= damage
        print(f"{self.name} took {damage} damage!")
        if self.current_health <= 0:
            self.current_health = 0
            self.status = "Dead"

    def get_health_status(self):
        return self.current_health


    def use_potion(self):
        potions = list(filter(lambda item: isinstance(item, Potion), self.inventory))
        if potions:
            print("Potions in my inventory:")
            for i, potion in enumerate(potions):
                print(f"{i + 1}: {potion.name}")


            index_of_potion = int(input("Choose the Potion: "))
            chosen_potion = potions[index_of_potion - 1]
            
            self.current_health += chosen_potion.healing_amount
            self.inventory.remove(chosen_potion)


            print(f"{self.name} use {chosen_potion.name} and healed {chosen_potion.healing_amount}:")
            return True
    
        print("You have no potions!")
        return False

def chance(success_rate: int) -> bool:
    return random.random() * 100 <= success_rate





