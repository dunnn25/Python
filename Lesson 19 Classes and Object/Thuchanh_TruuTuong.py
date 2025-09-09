# Tính chất trừu tượng - ABSTRACTION
from abc import ABC, abstractmethod

# Lớp trừu tượng
class Animal(ABC):
    # phương thức trừu tượng
    @abstractmethod
    def speak(self):
        pass
    # Ko phai la phuong thuc truu tuong
    def not_abstractmethod(self):
        print("Khong can ghi de lai")

# class con ke thua tu lop truu tuong
class Dog(Animal):
    def speak(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.speak())
my_dog.not_abstractmethod()