import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu ngẫu nhiên
data = np.random.randn(1000)

# figure,axes
fig, ax = plt.subplots()
ax.hist(data, bins=30, color="Black", edgecolor="Red", alpha=0.1) # bin: số lượng cột, alpha: độ trong suốt
# plt.hist(data, bins=30, color='skyblue', edgecolor='black')

plt.show()