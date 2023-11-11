#Write a Python program to create a class named Animal with an abstract method named sound. Implement subclasses for different animals, such as Dog, Cat, and Cow, and override the sound method for each subclass.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Bark"
class Cat(Animal):
    def speak(self):
        return "Meow"

class Cow(Animal):
    def speak(self):
        return "Moo"

dog= Dog()
print(dog.speak())
cat= Cat()
print(cat.speak())
cow= Cow()
print(cow.speak())