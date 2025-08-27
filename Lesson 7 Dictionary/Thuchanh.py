# Định nghĩa
# Dictionary là 1 datacolection và lưu data dưới dạng map (key và value)

# Khởi tạo
name_age = {"Min":5, "La":6, "Bong":10} 
# Tạo dic rỗng 
# name_age = dict()
# name_age = {}

# Truy cập
# print(name_age["Bong"])

# Thêm và dict, update giá trị
# name_age["Bong"] = 12
# name_age["Nam"] = 25
# print(name_age)

# Duyệt qua các phần tử của Dict
# Duyệt qua các keys
for k in name_age.keys():
    print(k)

# Duyệt qua các values
for k in name_age.values():
    print(k)

# Duyệt qua cả keys và values
for k, v in name_age.items():
    print(k,v)
