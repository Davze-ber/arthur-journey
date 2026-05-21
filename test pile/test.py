class Test:
    def __init__(self, name, resource_type,intelligence, hp, current_hp):
        self.intelligence = 5
        self.name = name
        self.resource_type = resource_type
        self.hp = hp
        self.current_hp = current_hp
  
        if self.resource_type == "rage":
            self.current_resource = 0
        else:
            self.current_resource = self.max_resource

    @property
    def max_resource(self):
        if self.resource_type == "rage":
            return 100
        
        if self.resource_type == "energy":
            return 120

        if self.resource_type == "mana":
            return 10+ self.intelligence

player1 = Test("t", "energy", 2, 10,10)        
player2 = Test("e", "energy", 2, 10,7)        
player3 = Test("s", "energy", 2, 10,5)        
player4 = Test("t*", "energy", 2, 10,2)        

def target(unit):
    ratio = (unit.current_hp/unit.hp) * 100
    print(ratio)
    if ratio >76 and ratio <= 100:
        return 1
    elif ratio >51 and ratio <= 75:
        return 2
    elif ratio > 26 and ratio <= 50:
        return 3
    elif ratio <= 25:
        return 4



team = [player1,player2, player3, player4]

def check_lowest_health(team):
    if not team:
        return None

    lowest_health = team[0]
    for unit in team[1:]:
        if unit.current_hp < lowest_health.current_hp:
            lowest_health = unit

    unit_index =  team.index(lowest_health)
    return lowest_health




name = input("│" + " Enter your name ".center(50) + "│ ")