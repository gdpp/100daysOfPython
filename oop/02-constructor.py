class Animal:
    legs = 4
    
    
class Dog:
    specie = "canine" #public attribute
    
    def __init__(self, name, breed, age, energy):
        self.name = name #instance attributes
        self.breed = breed
        self.age = age
        self._energy = energy
        self.__value = 1000000
    
    def bark(self):
        print(f"{self.name} is barking")
    
    def _waste_energy(self, qty):
        print(qty)
        self._energy -= qty
        
    def __get_value(self):
        return self.__value
        

dog1 = Dog("Jack", "Border Collie", 2, 100)
dog2 = Dog("Cali", "Mixed Breed", 2, 100)
dog3 = Dog("Sam", "Border Collie", 2, 100)

print(dog1)
print(dog1.name)
print(dog2.breed)
print(dog3.age)
print(dog3.specie)
dog1.bark()
dog2._waste_energy(10)
print(dog1._Dog__value)
print(dog3._Dog__get_value())

