import random

so_can_doan = random.randint(1,50)
so_nguoi_doan = 5
so_lan_doan = 5 # người dùng được dự đoán tối đa 5 lần

print("===============================================")
print("Game đoán số siêu khó")
print("Tôi đã chọn 1 số ngẫu nhiên từ 1 đến 50")
print("Bạn có " + str(so_lan_doan) + " lần đoán.")
print("===============================================")

while so_nguoi_doan != so_can_doan and so_lan_doan > 0:
    so_nguoi_doan = int(input("Nhập số bạn đoán: "))
    so_lan_doan -= 1
    if so_nguoi_doan < so_can_doan:
        print("Số bạn đoán nhỏ hơn số cần đoán.")
    elif so_nguoi_doan > so_can_doan:
        print("Số bạn đoán lớn hơn số cần đoán.")
    else:
        print("Chúc mừng bạn đã đoán đúng số!")
        break
    
    if so_lan_doan > 0:
        print("Bạn còn " + str(so_lan_doan) + " lần đoán nữa.")
        print("===============================================")
    else:
        print("Bạn đã hết lượt đoán.\n Số cần đoán là: " + str(so_can_doan))    
