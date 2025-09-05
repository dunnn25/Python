    # """
    # Loop in python
    
    # """

my_list = [1,2,3,4]
# for (Biết trước số lần lặp)
for iteam in my_list:
    print(iteam)

for i in range(len((my_list))):
    print(f"{i}: {my_list[i]}")

# While (Chưa rõ số lần lặp)
count = 1
while count<5:
    print("hello")
    count += 1    

# break, continue
for item in my_list:
    # print(item)
    if item == 3:
        #  break  (Duyệt đến vị trí item == 3 và dừng lại)
        continue # không duyệt qua item == 3 và tiếp tục duyệt qua các phần tử còn lại)
    print(item)

