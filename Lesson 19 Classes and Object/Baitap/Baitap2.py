###Bài 2: Hệ thống quản lý học sinh
class Student:
    def __init__(self,name,age,student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
    def add_grade(self,grade):
        self.grades.append(grade)
    def get_average_grade(self):
        a = sum(self.grades)
        b = len(self.grades)
        return a/b
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"student_id: {self.student_id}")
        print(f"Grades: {self.grades}")

Student1 = Student("Dung",21,2251262590)
Student1.add_grade(10)
Student1.add_grade(9)
Student1.display_info()
print(Student1.get_average_grade())
