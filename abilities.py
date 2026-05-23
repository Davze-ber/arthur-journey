class Ability():
    def __init__(self, name: str, resource: str, cost: int, main_stat: str, second_stat:str, primary_ratio: float, secondary_ratio:float, description: str):
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
        if self.main_stat in ["strenght, agility"]:
            return "Physical"
        elif self.main_stat == "intelligence":
            return "Magical"
        else:
            return "Other"

    
    def damage(self, unit) -> int:
        weapon_value = getattr(unit.gear.get("main_hand"), "damage", 0)
        primary_value = unit.total_stats[self.main_stat] * self.primary_ratio
        secondary_value = unit.total_stats[self.second_stat] * self.secondary_ratio


        return int(primary_value + secondary_value + weapon_value)

    def can_cast(self) -> bool:
        return self.current_resource >= self.cost

    def apply_cost(self, unit) -> None:
        unit.current_resource = max(0, unit.current_resource - self.cost) 