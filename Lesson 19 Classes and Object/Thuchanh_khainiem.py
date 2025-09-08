# #Phân biệt object và class
# Object: có trạng thái và hành vi
# class: template mô tả trạng thái và hành vi của loại đói tượng mà lớp hỗ trợ
# Khái niệm trong lập trình hướng đối tượng
# Constructor(hàm khởi tạo): Hàm gọi trong quá trình tạo object của class
# Atribute(thuộc tính): Là thành phần chứa dữ liệu trong class. Có 2 loại attribute là instance class và class Attribute
# Method(phương thức): có thể gọi là function in class 

# NOTE: class trong python

class Person:    
    # class attribute - dac trung cho toan bo class
    count = 0
    
    # hàm khởi tạo - constructor 
    def __init__(self,name,age):
        self.name = name     # self.name chính là instance attribute - gắn liền với từng đối tượng
        self.age = age    
        Person.count += 1
    
    # định nghĩa method - phương thức 
    def in_ra(self):
        print(f"Name: {self.name}   Age: {self.age}")
        
# tạo các đối tượng
per_1 = Person("Min", 20)
per_2 = Person("An", 30)

# print(Person.count)
# print("Name: ",per_1.name)
per_2.in_ra()        

"_____________________________________________________________________________________________________________________________"

 