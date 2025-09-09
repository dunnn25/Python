# Tính kế thừa là gì
# Tính kế thừa cho phép định nghĩa class mà kế thừa các phương thức và thuộc tính từ class khác

class Person:
    def __init__(self,name):
        self.name = name
    def printname(self):
        print(self.name)

my_stu = Person("Dung")
# Class con - class ke thua
class Student(Person):
    # Xay dung lai ham khoi tao
    def __init__(self, name, age):
        # self.name = name 
        super().__init__(name)
        # Person.__init__(self, name)
        self.age = age

my_stu = Student("Min",10)
my_stu.printname()
print(my_stu.age)  