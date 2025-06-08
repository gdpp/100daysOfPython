import random
from Enemy import *

class Ogre(Enemy):
    def __init__(self, health, attack):
        super().__init__(type="Ogre", health=health, attack=attack)
        
    def talk(self):
        print("*Ogre is slaming hands all around...*")
    
    def special_attack(self):
        special_attack_work =  random.random() < 0.2
        if special_attack_work:
            self.attack_damage += 4
            print("Ogre gets angry and increases attack by 4")