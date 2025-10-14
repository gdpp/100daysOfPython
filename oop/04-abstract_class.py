from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Sleeping")
    


