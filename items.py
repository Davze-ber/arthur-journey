class Item:
   def __init__(self, name, category,tag, value):
       self.name = name
       self.category = category
       self.value = value
       self.tag = tag




class Weapon(Item):
   def __init__(self, name, category, tag, value, damage):
       super().__init__(name, category, tag, value)
       self.damage = damage

class Armor(Item):
   def __init__(self, name, category, tag, value, armor):
       super().__init__(name, category, tag, value)
       self.armor = armor

class Potion(Item):
   def __init__(self, name, category,tag, value, healing_amount):
       super().__init__(name, category,tag, value)


       self.healing_amount = healing_amount





