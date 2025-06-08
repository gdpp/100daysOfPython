class Enemy:
    type_of_enemy: str
    health_points: int
    attack_damage: int
    
    def __init__(self, type, health, attack):
        self.__type_of_enemy = type
        self.health_points = health
        self.attack_damage = attack
    
    def get_type_of_enemy(self):
        return self.__type_of_enemy
    
    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")
    
    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")
        
    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage}")
        
    def special_attack(self):
        print("Enemy has no special attack!!!")