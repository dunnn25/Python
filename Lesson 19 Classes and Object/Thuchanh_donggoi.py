# NOTE đóng gói - inheritance

# class Student:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age

# # Tạo đối tượng
# my_stu = Student("Min", 20)

# print("Truoc khi thay doi: ",my_stu.name)
# my_stu.name = "An"
# print("Sau khi thay doi:", my_stu.name)

# NOTE: Sử dụng gạch dưới
# class Student:
#     def __init__(self,name,age):
#         self._name = name 
        
# # Tạo đối tượng
# my_stu = Student("Min", 20)

# print("Truoc khi thay doi: ",my_stu._name)
# my_stu._name = "An"
# print("Sau khi thay doi:", my_stu._name)

# NOTE: Sử dụng 2 dấu gạch dưới
class Student:
    def __init__(self,name,age):
        self.__name = name 
        
    def print_name(self):
        print("Name: ",self.__name)


# Tạo đối tượng
my_stu = Student("Min", 20)
# print("Truoc khi thay doi: ",my_stu.__name)
print(my_stu._Student__name)
# print("Truoc khi thay doi: ",my_stu._Student__name)
