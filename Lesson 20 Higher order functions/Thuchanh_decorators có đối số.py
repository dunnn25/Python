"""Decorator - TH  có arguments (đối số)"""
# NOTE Sử dụng higher-order function

# def decorator_func(func):
#     # hàm bao
#     def wrapper(name,age):
#         print("Before the function is called")
#         func(name,age)
#     return wrapper
# # hàm được bao
# def say_hello(name,age):
#     print(f"Hello {name}, you are {age} years old")

# my_func = decorator_func(say_hello)
# my_func("Min",15)
    
# NOTE áp dụng decorator

def decorator_func(func):
    # hàm bao
    def wrapper(name,age):
        print("Before the function is called")
        func(name,age)
    return wrapper

# hàm được bao
@decorator_func
def say_hello(name,age):
    print(f"Hello {name}, you are {age} years old")

say_hello("Min",15)
