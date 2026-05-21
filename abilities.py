class Ability():
    def __init__(self, name: str, resource: str, cost: int, main_stat: str, second_stat:str, primary_ratio: int, secondary_ratio:int,description: str):
        self.name = name
        cost.resource  = resource 
        self.cost = cost
        self.main_stat = main_stat
        self.second_stat = second_stat
        self.primary_ratio = primary_ratio
        self.secondary_ratio = secondary_ratio
        self. description = description

    

    @property
    def category(self) -> str:
        if main_stat in ["strenght, agility"]:
            return "Physical"
        elif main_stat == "intelligence":
            return "Magical"
        else:
            return "Other"

    
    def damage(self, unit: Character) -> int:
        weapon_value = getattr(unit.gear.get("main_hand"), "damage", 0)
        primary_value = unit.total_stats[self.main_stat] * self.primary_ratio
        secondary_value = unit.total_stats[self.second_stat] * self.secondary_ratio


        return int(primary_value + secondary_value + weapon_value)

    def subtracting_cost(self, unit:)