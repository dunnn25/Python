"""
Mathplotlib
"""
import matplotlib.pyplot as plt
import numpy as np

#Line plot -đường trong mathplotlib
# Tạo 2 numpy array
x = np.linspace(0,10,20) # 20 số từ 0 đến 10
y = np.linspace(0,20,20)

# Vẽ line plot
fig,ax = plt.subplots()   # Figure, Axes (vẽ đồ thị trong axes - ax)
fig.suptitle("Line plot", fontsize=16) 
# ax.plot(x,y)
# plt.show()

# Có thể truyền 1 array
# ax.plot(x)
# plt.show()

# Chỉnh màu sắc , lưu đồ thị, line style
# tuỳ chỉnh - Màu sắc - độ rộng - kiểu đường
ax.plot(x,y,color = "red", linewidth = 2, linestyle = ":")


# Cách lưu đồ thị NOTE phải lưu trước plt.show()
plt.savefig("mymathplotlib1.png")
plt.show()