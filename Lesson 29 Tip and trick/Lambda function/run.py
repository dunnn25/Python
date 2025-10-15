# def my_func(x,y):
#     return x+y

# print(my_func(4,6))

# my_func = lambda x, y: x+y
# print(my_func(4,6))


# sort list
# lst = ["Dung", "Mit", "Huong"]
# print(sorted(lst))
# print(sorted(lst, key=lambda x:len(x)))


# filter(func, iterable)
from hmac import new
from unittest import result


lst = [1,2,3,4,5,6]
new_lst = list(filter(lambda x: x%2 == 0, lst))
print(new_lst)


# map(func, iterable)
lst = [1,2,3,4,5,6]
new_lst = list(map(lambda x:x+3, lst))
print(new_lst)



# reduce(func, iterable)
from functools import reduce
lst = [1,2,3,4,5,6]
result = reduce(lambda x,y :x+y, lst)
print(result)