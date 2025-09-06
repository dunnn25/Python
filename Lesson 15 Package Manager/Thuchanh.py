import numpy as np

my_arr = np.array([[1,2],[3,4]])

my_new_ar =  my_arr.reshape(1,-1)

print(my_new_ar)

#Liệt kê các thư viện trong môi trường của mình
# pip list

# Tìm kiếm thư viện cụ thể trong môi trường 
# pip list | grep <tên thư viện>    #Chạy linux thôi

# Lưu packages ra files
# pip freeze > requirements.txt


# Cài thư viện từ file requirement.txt
# pip install  -r requirement.txt

# ----------------------------------------- #
"Conda"
