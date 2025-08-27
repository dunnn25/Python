# #1. Tạo set
# my_set = {'a','b'}
# my_set = set()     # Tạo set rỗng 
# print(my_set)
# print(type(my_set))

# #2. Không cho phép lập lại các phần tử
my_set = {'a','b','a','b'}
print(my_set)

# #3. Check set là unorder (mỗi lần chạy lại thứ tự sẽ khác nhau)
# my_set = {'a','b','c','d'}
# for item in my_set:
#     print(item)

# #4. Update các phần tử trong set
# my_set = {'a','b','a','b'}
# my_set.add('e') #Thêm phần tử
# my_set.discard('a') #Xoá phần tử trong set
# print(my_set)

#5. Thao tác với 2 hay nhiều sets, xem thêm sơ đồ Venn
my_set1= {'a','b','c','d'}
my_set2 = {'c','d','e','f'}

# new_set = my_set1.intersection(my_set2) # Giao của 2 set
# new_set = my_set1.union(my_set2)          # Hợp của 2 set
new_set = my_set1.symmetric_difference(my_set2) # Lấy ra phần tử khác nhau của 2 set
print(new_set)


