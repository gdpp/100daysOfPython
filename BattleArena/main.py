from Enemy import *
from Zombie import *
from Ogre import *

def battle(en1: Enemy, en2: Enemy):
    en1.talk()
    en2.talk()
    
    while en1.health_points > 0 and en2.health_points > 0:
        print('------------')
        en1.special_attack()
        en2.special_attack()
        print(f"{en1.get_type_of_enemy()}: {en1.health_points} HP left")
        print(f"{en2.get_type_of_enemy()}: {en2.health_points} HP left")
        en2.attack()
        en1.health_points -= en2.attack_damage
        en1.attack()
        en2.health_points -= en1.attack_damage
        print("-------------")
        
    if en1.health_points > 0:
        print(f'{en1.get_type_of_enemy()} wins!')
    else:
        print(f'{en2.get_type_of_enemy()} wins!')

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie, ogre)