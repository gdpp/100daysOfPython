class Animal:
    def __init__(self, name, age):
        self.name = name
        
    def sound(self):
        print(f"{self.name} makes a noise")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        
    def sound(self):
        super().sound()
        print(f"{self.name} baarks!")
    

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def sound(self):
        super().sound()
        print(f"{self.name} meeoow!")