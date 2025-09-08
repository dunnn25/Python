""" Xử lý ngoại lệ """

# my_dict = {"age":10,"name":"dung"}
# try:
#     result = 10/0
#     my_value = my_dict["add"]
    
# except ZeroDivisionError:
#     print("Loi chia cho 0")
# except KeyError:
#     print("Loi keyerror")
# print("Bye bye")

try:
    num = int(input("Nhap vao mot so nguyen: "))
    result = 100/num
except:
    print("Cu co loi la vao day")    

# except ZeroDivisionError:
#     print("Không thể chia cho 0")
# except ValueError:
#     print("Sai kieu du lieu")

else:
    print("Nhap so ok, phep chia ok")
    print(f"Ket qua:{result}")

finally:
    print("Di vao day bat ke co loi hay khong")