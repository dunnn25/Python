import pandas as pd

data = pd.read_csv('C:\\workspace\\30 Days of code the compelete python\\Lesson 22 Pandas\\data.csv')
# print(data.head( )) # in ra 5 dòng đầu tiên
# print(data.tail( )) # in ra 5 dòng cuối cùng
# print(data.info( )) # in ra thông tin về dataframe
# print(data.describe( )) # in ra các thông tin thống kê về dataframe
# print(data.shape) # in ra kích thước của dataframe (số hàng, số cột)

# # Lưu lại file
# data.to_csv('C:\\workspace\\30 Days of code the compelete python\\Lesson 22 Pandas\\data1.csv', index=False) # index=False để không lưu lại chỉ số của các dòng

## Insprect data
print(data.info()) # in ra thông tin về dataframe
print(data.describe())  # in ra các thông tin thống kê về dataframe

##  
