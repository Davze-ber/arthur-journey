class Item:
    def __init__(self, name: str, category: str, tag: str, value: int):
        self.name = name
        self.category = category
        self.value = value
        self.tag = tag

    def clone(self):
        return Item(self.name, self.category, self.tag, self.value)

class Equippable(Item):
    def __init__(self, name: str, category: str, tag: str, value: int = 0, health:int = 0, strength:int = 0, agility:int = 0, intelligence:int = 0, defense:int = 0, speed:int = 0):
        super().__init__(name, category, tag, value)
        self.stats: dict[str,int] = {
            "health" : health,
            "strength" : strength,
            "agility" : agility,
            "intelligence" : intelligence,
            "defense" : defense,
            "speed" : speed
        }

    def clone(self):
        return type(self.name, self.category, self.tag, self.value, **self.stats)
    
class Weapon(Equippable):
    def __init__(self, name: str, category: str, tag: str, value: int = 0, health:int = 0, strength:int = 0, agility:int = 0, intelligence:int = 0, defense:int = 0, speed:int = 0, weapon_damage: int = 0, spell_damage: int = 0):
        super().__init__(name, category, tag, value, health, strength, agility, intelligence, defense, speed)
        self.weapon_damage = weapon_damage
        self.spell_damage = spell_damage

    def clone(self):
        return Weapon(self.name, self.category, self.tag, self.value, **self.stats, weapon_damage=self.weapon_damage, spell_damage=self.spell_damage
                      )
class Armor(Equippable):
    def __init__(self, name: str, category: str, tag: str, value: int = 0, health:int = 0, strength:int = 0, agility:int = 0, intelligence:int = 0, defense:int = 0, speed:int = 0):
        super().__init__(name, category, tag, value, health, strength, agility, intelligence, defense, speed)
        
class Shield(Equippable):
    def __init__(self, name: str, category: str, tag: str = "off_hand", value: int = 0, health:int = 0, strength:int = 0, agility:int = 0, intelligence:int = 0, defense:int = 0, speed:int = 0, block_chance:int = 0):
        super().__init__(name, category, tag, value, health, strength, agility, intelligence, defense, speed)
        self.block_chance = block_chance

    def clone(self):
        return Shield(self.name, self.category, self.tag, self.value,self.block_chance **self.stats)
        
class Potion(Item):
    def __init__(self, name: str, category: str,tag: str, value: int, healing_amount: int = 0, restore_mana: int = 0):
        super().__init__(name, category,tag, value)
       
        self.healing_amount = healing_amount
        self.restore_mana = restore_mana
        
    def clone(self):
        return Potion(self.name, self.category, self.tag, self.value, self.healing_amount, self.restore_mana)

        
class StackAble(Item):
    def __init__(self, name: str, category: str, tag: str, value: int, can_stack: bool =False, amount: int = 1):
        super().__init__(name, category, tag, value)
        self.can_stack = can_stack
        self.amount = amount
    
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.name == other.name 

    @property
    def total_value(self):
        return self.amount * self.value
    
    def clone(self):
        return type(self)(
            self.name,
            self.category,
            self.tag,
            self.value,
            self.can_stack,
            self.amount
        )
    
class Junk(StackAble):
    def __init__(self, name: str, category: str, tag:str, value: int, can_stack: bool = True, amount: int = 1):
        super().__init__(name, category, tag, value, can_stack, amount)

class Material(StackAble):
    def __init__(self, name: str, category: str, tag: str, value: int, can_stack: bool = True, amount: int = 1):
        super().__init__(name, category, tag, value, can_stack, amount)







def check_arrows_in_quiver(new_arrows, player_quiver):
    if new_arrows.can_stack and new_arrows in player_quiver:
        index_arrow = player_quiver.index(new_arrows)
        player_quiver[index_arrow].amount += new_arrows.amount
    else:
        player_quiver.append(new_arrows)