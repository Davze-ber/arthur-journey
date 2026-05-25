class Item:
    def __init__(self, name: str, category: str, tag: str, value: int):
        self.name = name
        self.category = category
        self.value = value
        self.tag = tag

class Equippable(Item):
    def __init__(self, name: str, category: str, tag: str, value: int = 0, health:int = 0, strength:int = 0, agility:int = 0, intelligence:int = 0, defence:int = 0, speed:int = 0):
        super().__init__(name, category, tag, value)
        self.stats: dict[str,int] = {
            "health" : health,
            "strength" : strength,
            "agility" : agility,
            "intelligence" : intelligence,
            "defence" : defence,
            "speed" : speed
        }

class Weapon(Equippable):
    def __init__(self, name: str, category: str, tag: str, value: int = 0, health:int = 0, strength:int = 0, agility:int = 0, intelligence:int = 0, defence:int = 0, speed:int = 0, damage: int = 0):
        super().__init__(name, category, tag, value, health, strength, agility, intelligence, defence, speed)
        self.damage = damage

class Armor(Equippable):
    def __init__(self, name: str, category: str, tag: str, value: int = 0, health:int = 0, strength:int = 0, agility:int = 0, intelligence:int = 0, defence:int = 0, speed:int = 0):
        super().__init__(name, category, tag, value, health, strength, agility, intelligence, defence, speed)
        

class Potion(Item):
    def __init__(self, name: str, category: str,tag: str, value: int, healing_amount: int):
        super().__init__(name, category,tag, value)

        self.healing_amount = healing_amount





