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
        self.backpack_size = 2
        self.inventory = []
    


    @property
    def attack(self):
        return self.power + self.bonus_attack


    def receive_attack(self, opponent):
        incoming_damage = opponent.attack + random.randint(-2,+2)
        damage = max(0, incoming_damage - self.defence)
        self.current_health -= damage
        print(f"{self.name} took {damage} damage!")
        if self.current_health <= 0:
            self.current_health = 0
            self.status = "Dead"
            print(f"{self.name} has fallen!")




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





