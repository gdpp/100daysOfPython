import random
from Enemy import *

class Zombie(Enemy):
    def __init__(self, health, attack):
        super().__init__(type="Zombie", health=health, attack=attack)
        
    def talk(self):
        print("*Grumbling...*")
        
    def spread_disease():
        print("The zombie is trying to spread infection.")
    
    def special_attack(self):
        special_attack_work =  random.random() < 0.5
        if special_attack_work:
            self.health_points += 2
            print("Zombie regenerated 2 HP")