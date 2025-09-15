import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Jane', 'Mike', 'Sarah'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# iloc - sẽ dựa theo index của hàng và cột 
# loc - sẽ dựa theo tên của hàng và cột - tên cột và tên hàng
# print(df.loc[0])
# print(df.loc[[0,2]]) # lấy ra 2 hàng 

# Kết hợp hàng với cột
# Chọn tất cả các hàng với 1 cột
# print(df.loc[:,['Name','City']])
# print(df.loc[0, 'Name'])



# Phương thức iloc
# print(df.iloc[0]) # lấy ra hàng đầu tiên
# print(df.iloc[0:2]) # lấy ra 2 hàng đầu tiên

# print(df.iloc[:, [0,2]] )

# Có thể tự set labels (index) cho hàng
newdt_df = df.set_index('Name')
print(newdt_df)

print(newdt_df.loc['John'])