# functions trong python được coi như là first class citizens:
# Có thể truyền ở dạng tham số đối số
# Trả về giá trị từ chúng

'''Higher order functions'''

# NOTE: Take one or more functions as arguments - Nhận function làm tham số
def cal_sum(nums): # hàm thông thường
    return sum(nums)

def higher_order_func(my_func, my_list): # cal_sum sẽ chính là tham số được truyền vào cho my_func
    my_sum = my_func(my_list)
    return my_sum

my_result = higher_order_func(cal_sum, [3,4,5])
print("My sum: ", my_result)

#NOTE: Return a function as its result - trả về function 
# Trả về hàm trong hàm 
def cal_min(a,b):
    if a<b:
        return a
    else:
        return b
    
def cal_max(a,b):
    if a>b:
        return a
    else:
        return b

# đi tạo higher order function và trong này sẽ trả về hàm thông thường     
def higher_oder_function(cal_name):
    if cal_name == "min":
        return cal_min
    elif cal_name == "max":
        return cal_max

# NOTE: Muốn đi tính min của 2 số 
my_result = higher_oder_function("min")
print(my_result(3,5))
# NOTE: Muốn đi tính max của 2 số 
my_result = higher_oder_function("max")
print(my_result(3,5))