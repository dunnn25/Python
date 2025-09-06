# Tạo list bằng for (thông thường)
# list = [1,2,3,4,5]
# new_lst = []
# for x in list:
#     new_lst.append(x ** 2)
# print(new_lst)

# list comprehension
# list = [1,2,3,4,5]
# new_lst = [x ** 2 for x in list]
# print(new_lst)

# filter element (lọc các phần tử)
# [expression for item in iterable if condition == True]
# list = [1,2,3,4,5]
# new_lst =  [x for x in list if x%2 == 1] 
# print(new_lst)

# apply function to each element 
# [expression_1 if condition == True else expression_2 for item in iterable ]
# list = [1,2,3,4,5]
# new_lst = [ x if x%2 == 0 else x + 2 for x in list] 
# print(new_lst)

# """ dictionary comprehension """
# {k: v for item in iterable}
# lst = [1,2,3,4,5]
# new_dict = {k: k** 2 for k in lst}
# print(new_dict) 

# """ set comprehension """
# {item for item in iterable}
# my_string = """Tao la bo"""
# new_set = {letter for letter in my_string}
# print(new_set)

# """Multiple loops"""
nested_lst = [[i for i in range(5)] for _ in range (5)]
print(nested_lst)

arr_2d = [
    [1,2,3],
    [4,5,6],
    [7,7,8]
]
# flatten_lst = [num for row in arr_2d for num in row] #list comprehention
# print(flatten_lst)

new_text = []
for row in arr_2d: # dùng 2 vòng lặp for
    for num in row:
        new_text.append(num)
print(new_text)