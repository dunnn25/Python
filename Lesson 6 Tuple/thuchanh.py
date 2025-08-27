# Tuple trong python
# 1. Tạo tuple
tuple_1 = ("a", 3) # Nhớ 1 phần tử thì thêm dấu phẩy
print(tuple_1)
print(type(tuple_1))


# Duyệt qua các phần tử của tuple
tuple_1 = ("a", 3, 4, "b") # Nhớ 1 phần tử thì thêm dấu phẩy

print(f"Chiều dài của tuple: {len(tuple_1)}")
for item in tuple_1:
    print(item)
    
print(tuple_1[3])

#3. Công tuple
tuple_1 = ("a", 3, 4, "b") # Nhớ 1 phần tử thì thêm dấu phẩy
tuple_2 = ("c", 5, 6, "db") # Nhớ 1 phần tử thì thêm dấu phẩy

new_tuple = tuple_1+tuple_2
print(f"New tuple: {new_tuple}")

#4. Thêm sửa xoá tuple
tuple_1 = ("a", 3, 4, "b") # Nhớ 1 phần tử thì thêm dấu phẩy
list_1 = list(tuple_1)
# list_1.append("Hello")
list_1.remove(4)

new_tuple = tuple(list_1)
print(new_tuple)

tuple_1 = ("a", 3, 4, "b") # Nhớ 1 phần tử thì thêm dấu phẩy
# Trả về số lần xuất hiện của phần tử
print(tuple_1.count("5"))
# Trả về index
print(tuple_1.index(3))

tuple_2 = ("a", 3, 4, "b")

print(F"ID of tuple_1: {id(tuple_1)}" )
print(F"ID of tuple_2: {id(tuple_2)}" )

# Cách thay đổi giá trị với tuple
tuple_1 = ([1,2,3], 3, 4, "b", "c")

tuple_1[0][0] = "a"
print(tuple_1)