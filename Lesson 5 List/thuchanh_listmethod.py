## Methods of list

# 1. Add list element (1 element) .append() {Thêm phần tử vào cuối}
my_lst = [1, 3, 6, 10, -5]
my_lst.append(50)
print(my_lst)
# 2. Add multiple elements .extend() {Mở rộng list}
print("------Mở rộng list------")
my_lst = [1, 3, 6, 10, -5]
lst_1 = ["Anh", "Em"]
my_lst.extend(lst_1)
print(my_lst)

# 3. Sort list .sort() or sorted()
print("------Sắp xếp list------")
my_lst = [1, 3, 6, 10, -5]
my_lst.sort()
print("Sắp xếp theo chiều tăng dần",my_lst)
my_lst.sort(reverse=True)
print("Sắp xếp theo chiều giảm dần: ",my_lst)
new_lst = sorted(my_lst) # my_lst không đổi
print(new_lst)

# 4. Reverse list
print("------Đảo ngược list------")
my_lst = [1, 3, 6, 10, -5]
my_lst.reverse()
print(my_lst)
# or
new_lst = my_lst[::-1]
print(new_lst)
# 5. Insert element .insert(index, value)
print("------Chèn phần tử trong list------")
my_lst = [1, 3, 6, 10, -5]
my_lst.insert(0, 100) #insert(vị trí, giá trị chèn)
print(my_lst)

# 6. Delete element del or .remove(ele)
print("------Xoá phần tử trong list------")
my_lst = [1, 3, 6, 10, -5]
del my_lst[2]
print(my_lst)
del my_lst[:2] # Xoá nhiều phần tử
print(my_lst)
# 7. Return the first index of a matched element .index() (no error if not found)
print("------trả về phần tử trong list------")
my_lst = [1, 3, 6, 10, -5]
ind = my_lst.index(10)
print(ind)

# 8. Remove element by index .pop(index) (if no index is given, removes the last element)
print("------Xoá phần tử trong list------")
my_lst = [1, 3, 6, 10, -5]
ele = my_lst.pop(3) # Thiết lập phần tử bị xoá
print(ele) # Trả về phần tử bị xoá
print(my_lst)
