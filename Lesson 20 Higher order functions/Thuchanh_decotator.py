"""Decorator - TH không có arguments (đối số)"""

#NOTE: dùng higher-order function thông thường

# NOTE wrapper(hàm bao)

# dùng higher order function để thay đổi tính năng của wrapped
def decorator_example(func):
    def wrapped():
        print("Before the function is called")
        func()
        print("After the function is called")
    
    return wrapped

@decorator_example #chỉ sử dụng khi áp dụng decorator
def say_hello():     # hàm được bao
    print("Hello")

    """
    say_hello tương đương với decorator_example(say_hello)
    say_hello() = warapper()
    """
#NOTE sử dụng higher order function nguyên bản    
# my_func = decorator_example(say_hello)
# my_func()

#NOTE: sử dụng decorator
say_hello()  # gọi trực tiếp hàm được bao

    
