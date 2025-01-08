"""Oops concept
write a class to explain Polymorphism (method overloading and over-riding)
Write a class to explain inheritance
write a class to explain Abstraction
Write a class to explain Encapsulation (using private and protected variables)"""
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return "Hello from Child"

obj1 = Parent()
obj2 = Child()
print(obj1.greet())
print(obj2.greet())

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

print(Dog().speak())

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

print(Circle(5).area())

class Person:
    def __init__(self, name, age):
        self._name = name  # Protected
        self.__age = age  # Private

    def get_age(self):
        return self.__age

p = Person("John", 30)
print(p.get_age())
