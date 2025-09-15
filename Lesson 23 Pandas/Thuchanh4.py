import pandas as pd
data = pd.DataFrame({'Name': ['John', 'Jane', 'Bob'], 'Age': [25, 30, 35]})

data['Salary'] = [50000, 60000, None]
print(data)
print(data.info())
print(data.isnull())

# data['Salary'] = data['Salary'].fillna(data['Salary'].mean())  # Thay thế giá trị thiếu bằng 0
# print(data)
# print(data.info())
# print(data.isnull())

# Xoá các hàng có ô không có giá trị 
new_data = data.dropna()
print(new_data)