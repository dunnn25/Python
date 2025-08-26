# my_str = "Hello"
# print(my_str)
# print(type(my_str))

# Chiều dài str len()
# print(len(my_str))

# Truy cập đến kí tự => index
# # index dương: 0 --> len(str)-1
# print(my_str[4])
# # index âm: -len(str) => -1
# print(my_str[-2])

# # Slicing for string
# print(my_str[1:4])   # index: 1, 2, 3
# print(my_str[1:])
# print(my_str[:-1])   # Không bao gồm index -1

# Nối chuỗi 
# str_1 = "I"
# str_2 = "Love You"
# concat_str = str_1 + str_2
# print(concat_str)

# Duyệt qua các kí tự trong chuỗi 
# my_str = "Hello"
# for ch in my_str:
#     print(ch)

# Kiểm tra chuỗi con có trong chuỗi không?
# my_str = "Helllllllooo"
# if "Helllllllooo" in my_str:
#     print("OK")
# else:
#     print("Đéo có ")

# Methods
# my_str = "Hello anh em"
# print(my_str.upper())   # in hoa chuỗi 
# print(my_str.lower())   # in thường chuỗi

# String is immutable in Python (Không thể thay đổi kí tự trong chuỗi đã được định nghĩa)
my_str = "Hellllo"
# my_str[1] = "E" (Không thể thay đổi kí tự trong chuỗi đã được định nghĩa)
my_str = "Hello"
print(my_str)
