def timer_decorator(func):
    def wrapper(*args,**kwargs):
        import time
        time_start = time.time()
        result = func(*args,**kwargs)
        time_end = time.time()
        print(f"Thời gian thực thi của hàm là {time_end - time_start}")
        return result
    return wrapper

@timer_decorator
def tong(number):
    return sum(number)

total = tong([9999999999999999999,9999999999999999999999,999999999999999999999999999])


        
        
        