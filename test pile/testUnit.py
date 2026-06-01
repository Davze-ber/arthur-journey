class Dummy():
    def __init__(self,name, hp, max_health, res_type, res_max):
        
        self.name =name
        self.hp = hp
        self.max_health = max_health
        self.res_type = res_type
        self.res_max = res_max

    def apply_potion_effect(self, source) -> None:
        if hasattr(source,"health"):
            heal_amount = getattr(source, "healing_amount", 0)
            self.current_health = min(self.current_health + heal_amount, self.max_health)
        elif hasattr(source,"mana"):
            if self.resource_type == "mana":
                mana_amount = getattr(source, "restore_mana", 0)
                self.resource = min(self.current_resource + mana_amount, self.max_resource)
                
class MockHealthPotion:
    def __init__(self, health):
        self.health = health

class MockManaPotion:
    def __init__(self, mana):
        self.mana = mana

def test_apply_potion_effect():
    # Setup: Create a player with 50/100 HP and 10/100 Mana
    # Assume Arthur is an instance of your Archer/Warrior class
    arthur = Unit(name="Arthur", hp=100, res_type="mana", res_max=100)
    arthur.current_health = 50
    arthur.current_resource = 10

    # Test Case 1: Health Potion
    h_potion = MockHealthPotion(health=30)
    arthur.apply_potion_effect(h_potion)
    print(f"Health after potion: {arthur.current_health}") # Should be 80
    
    # Test Case 2: Health Overheal (Clamping)
    big_h_potion = MockHealthPotion(health=500)
    arthur.apply_potion_effect(big_h_potion)
    print(f"Health after overheal: {arthur.current_health}") # Should be 100

    # Test Case 3: Mana Potion
    m_potion = MockManaPotion(mana=20)
    arthur.apply_potion_effect(m_potion)
    print(f"Mana after potion: {arthur.current_resource}") # Should be 30

# Run the test
test_apply_potion_effect()
