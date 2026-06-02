class Ability():
    def __init__(self, name: str, resource: str, cost: int, main_stat: str = 0, second_stat:str = 0, primary_ratio: float = 0, secondary_ratio:float = 0, description: str = ""):
        self.name = name
        self.resource  = resource 
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
        bonus_damage = 0
        primary_value = unit.total_stats[self.main_stat] * self.primary_ratio
        secondary_value = unit.total_stats[self.second_stat] * self.secondary_ratio
        if unit.resource_type in ["rage", "energy"]: 
            bonus_damage = getattr(unit.gear.get("main_hand"), "weapon_damage", 0)
          
        if unit.resource_type in ["mana"]:
            bonus_damage = getattr(unit.gear.get("main_hand"), "spell_damage", 0)

        return int(primary_value + secondary_value + bonus_damage)

        

    def can_cast(self, unit) -> bool:
        return unit.current_resource >= self.cost

    def apply_cost(self, unit) -> None:
        unit.current_resource = max(0, unit.current_resource - self.cost) 