# import numpy as np
# arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])    
# print(arr_2d)
# print(arr_2d[0,0])  # truy cập phần tử hàng 1 cột 1
# print(arr_2d[1,2])  # truy cập phần tử hàng 2 cột 3
# print(arr_2d[2,2])  # truy cập phần tử hàng 3 cột 3  
# print(arr_2d[0]) # Truy cập hàng đầu tiên
# print(arr_2d[:,0]) # Truy cập cột đầu tiên

## Các tính chất ndim,shape,size và cách chuyển kiểu dữ liệu
import numpy as np

arr_1d = np.array([1,2,3])
print(arr_1d.dtype)
# arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

# # ndim - số chiều của numpy array
# print("Số chiều của mảng 1:",arr_1d.ndim) 
# print("Số chiều của mảng 2:",arr_2d.ndim)

# # Shape - kích thước của mảng - trả về TUPLE
# print("Kích thước của mảng 1:",arr_1d.shape) 
# print("Kích thước của mảng 2:",arr_2d.shape)

# # Size - số phần tử của mảng
# print("Số phần tử của mảng 1:",arr_1d.size) 
# print("Số phần tử của mảng 2:",arr_2d.size)

# # Chuyển kiểu dữ liệu
# arr_1d_float = arr_1d.astype(np.float64)

# print(arr_1d_float)
# print(arr_1d_float.dtype)

## Tạo numpy array theo mẫu, chỉ định kiểu khi tạo

# # tạo mảng array giá trị toàn 0
import numpy as np
# zeros_arr = np.zeros((3,4) )
# print(zeros_arr)

# # tạo array toàn 1
# one_arr = np.ones((3,4))
# print(one_arr)

# # tạo array chuỗi các giá trị liên tiếp nhau
# new_arr = np.arange(19)
# print(new_arr)

# new_arr2 = np.arange(0, 11, 2)     # truyền vào 3 giá trị  - Không lấy phần tử cuối
# print(new_arr2)


# # linespace
# new_arr = np.linspace(0, 10, num=5)   # tạo array với 5 giá trị cách đều từ 0 đến 10 (Bao gồm cả phần tử đầu và cuối)
# print(new_arr)

# x = np.ones((2,)) # mặc định luôn là float64
# y = np.ones((2,), dtype=np.int32) # truyền vào kiểu dữ liệu
# print(x)
# print(y)
# print(x.dtype)
# print(y.dtype)

# ## Các phép toán số học với numpy array
# arr_1 = np.array([1,2,3])
# arr_2 = np.array([4,5,6])

# # Phép cộng
# result = arr_1 + arr_2
# print(result) # Kết quả là [5,7,9]

# # Phép trừ
# result = arr_1 - arr_2
# print(result) # Kết quả là [-3,-3,-3]

# # Phép nhân
# result = arr_1 * arr_2
# print(result) # Kết quả là [4,10,18]    

# # Phép chia 
# result = arr_1/arr_2
# print(result) # Kết quả là [0.25,0.4,0.5]
# print(result.dtype) # Kết quả là float64

# Tính trung bình
arr_1 = np.array([1,2,3])
print("Max: ", arr_1.max())
print("Min: ", arr_1.min())
print("Mean: ", arr_1.mean())

# Tính tổng các phần tử trong array
arr_1 = np.array([1,2,3])
print("Tổng của các phần tử: ", arr_1.sum())
print("Tổng của các phần tử: ", np.sum(arr_1))  # Cách khác để tính tổng

arr_2d = np.array([[1,2,3],[7,8,9]])
print("Tổng của từng hàng: ",arr_2d.sum(axis=1))
print("Tổng của từng cột: ",arr_2d.sum(axis=0))

# Khi muốn giữ số chiều giống như array ban đầu
row_sum = arr_2d.sum(axis=1, keepdims=True)
col_sum = arr_2d.sum(axis=0, keepdims=True)
print(row_sum.shape)
print(col_sum.shape)