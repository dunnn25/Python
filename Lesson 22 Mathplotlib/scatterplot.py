import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu ngẫu nhiên
x = np.linspace(0,5,20)
y = np.linspace(0, 10 ,20)

# Vẽ scatter plot
fig, ax = plt.subplots()
# ax.scatter(x, y, marker='+', color='palevioletred', s=100, alpha=0.5) # s: kích thước điểm, alpha: độ trong suốt
ax.plot(x,y, marker='o', color='darkcyan', linestyle='--')
plt.show()
