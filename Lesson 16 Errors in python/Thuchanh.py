# Các lỗi thường gặp
# NOTE Syntax Error : Lỗi cú pháp
# print( "xin chao cac ban")

# NOTE NameError : Sử dụng biến hoặc function mà chưa định nghĩa 
# myvar = "xinchaocacban"
# print( myvar)


# NOTE IndexError : Nếu index vượt ngoài phạm vi thì sẽ báo lỗi
# my_lst = [1,2,3,4]
# print(my_lst[-4])

# # NOTE ModuleNotFoundError : Nỗi module chưa cài đặt
# import numpy as np
# my_arr = np.array([1,3,3])
# print(my_arr)

# # NOTE AttributeError: Khi truy cập vào 1 attribute không tồn tại trong method đấy
# my_lst = [1,2,4]

# my_lst.append("value")
# print(my_lst)

# # NOTE KeyError (Truy cập vào key value mà không tồn tại trong dictionary):
# my_dict = {"name": "Min", "age":10, "address":"Hanoi"}
# print(my_dict["address"])


# # NOTE TypeError (Sai kiểu dữ liệu):
# num = 10
# print(num + "anh em")
# NOTE ImportError (import 1 module từ thư viện mà không tồn tại trong thư viện đó):
# from numpy import module
from numpy import random
random.seed(1)
print(random.randint(1,100))
# NOTE ValueError (Xảy ra khi 1 function nhận vào tham số đúng kiểu dữ liệu nhưng giá trị tham số lại không hợp lệ):
num = int("123")
print(num)
# NOTE ZeroDivisionError (Báo lỗi khi chia cho 0) :
print(10 / 0 )