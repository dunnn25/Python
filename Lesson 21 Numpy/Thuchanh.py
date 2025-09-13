# # # Numpy là gì ?: Numpy là 1 thư viện nền tảng thực hiện phân tích dữ liệu trong python
# # Numpy giúp chúng ta làm việc với ndarrays 
# Axits trong numpy: Với array 1 chiều axits mặc định là 0
# NOTE Với array nhiều chiều axits có axits là 0(dọc) và 1(ngang)
# Trong numpy tất cả các phần tử đều thuộc 1 kiểu dữ liệu

"""CODE"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5.5]) # tất cả các phần tử đều được ép về 1 kiểu dữ liệu

# print(arr)
# print(type(arr))
# print(arr.dtype)

#Truy cập các phần tử
print(f"Phần tử đầu tiên của mảng {arr[0]}")
print("Phần tử cuối cùng của bản", arr[4],arr[-1])

# Slicing
print(arr[1:4])
print(arr[:3])

# Slicing không tạo ra bản copy mà chỉ trả về view có nghĩa nó vẫn dùng chung địa chỉ dựa trên array ban đầu
new_arr = arr
print(new_arr)
new_arr[0] = 100   
print(new_arr)
print(arr) # Slicing không tạo ra bản copy mà chỉ trả về view

