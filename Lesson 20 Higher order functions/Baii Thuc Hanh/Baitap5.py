def call_limit_decorator(limit):
    count = 0
    def wrapper(func):
        def inner_function(*args,**kwargs):
            nonlocal count
            if count < limit:
                count += 1
                print(f"Bạn vẫn có thể gọi {limit - count} lần hàm nữa")
                return func(*args,**kwargs)
            else:
                print(f"Số lần gọi của bạn đã vượt quá số lần quy định \nBạn có {limit} lần gọi")
        return inner_function
    return wrapper
@call_limit_decorator(limit=2)
def Say_hello():
    print("Helllo")

Say_hello()
Say_hello()
Say_hello()
