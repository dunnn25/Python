# TÍNH ĐA HÌNH _ POLYMORPHISM


# class Cow:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name + " say moo"


# class Cat:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         return self.name + " say meomeo"

# my_cow = Cow("Bo")
# my_cat = Cat("Cat")

# print(my_cow.speak())
# print(my_cat.speak())

class Animal:
    def speak(self):
        return "some sound"

class Dog(Animal):
    def speak(self):
        return "woof!"

my_ani = Animal()
my_dog = Dog()

# print(my_ani.speak())
print(my_dog.speak())

 