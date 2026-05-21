  def receive_attack(self, opponent):
        incoming_damage = opponent.attack + random.randint(-2,+2)
        damage = max(0, incoming_damage - self.total_stats[defence])
        self.current_health -= damage
        print(f"{self.name} took {damage} damage!")
        if self.current_health <= 0:
            self.current_health = 0
            self.status = "Dead"