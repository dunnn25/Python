import numpy as np

arr_1 = np.array([[1,2,3],[4,5,6]])

new_arr = np.reshape(arr_1,(3,2)) # chuyển thành 3 hàng 2 cột
print(new_arr)
print(new_arr.shape)

new_arr = arr_1.reshape(6) # chuyển thành 1 chiều
print(new_arr)

new_arr = arr_1.flatten() # chuyển thành 1 chiều
print(new_arr)