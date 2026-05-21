class Item:
    def __init__(self, name: str, category: str, tag: str, value: int):
        self.name = name
        self.category = category
        self.value = value
        self.tag = tag

class Weapon(Item):
    def __init__(self, name: str, category: str, tag: str, value: int, damage: int):
        super().__init__(name, category, tag, value)
        self.damage = damage

class Armor(Item):
    def __init__(self, name: str, category: str, tag: str, value: int, armor: int):
        super().__init__(name, category, tag, value)
        self.armor = armor

class Potion(Item):
    def __init__(self, name: str, category: str,tag: str, value: int, healing_amount: int):
        super().__init__(name, category,tag, value)

        self.healing_amount = healing_amount





