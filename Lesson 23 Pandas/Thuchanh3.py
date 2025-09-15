import pandas as pd

data = pd.DataFrame({'Name': ['John', 'Jane', 'Bob'], 'Age': [25, 30, 35]})
# print(data)

# print(data['Name'])


# Filter row based on condition - Lọc các hàng dựa trên điều kiện
# filtered = data[data['Age'] > 30]
# print(filtered)

# Thay đổi dữ liệu trong dataframe
# Thêm cột mới
data['City'] = ['New York', 'Los Angeles', 'Chicago']
print(data)

# Xoá cột city
new_data = data.drop('City', axis=1) # axis=1 là xoá cột, axis=0 là xoá hàng
print(new_data)

# Thay đổi giá trị ở một ô cụ thể
data.loc[0, 'Age'] = 26
print(data)