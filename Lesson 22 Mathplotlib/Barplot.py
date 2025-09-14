import matplotlib.pyplot as plt
import numpy as np

labels = ["Class_A","Class_B","Class_C"]
counts =[23,17,35]
sort = np.sort([labels ])
colors = ['red', 'blue', 'green']

fig, ax = plt.subplots()
# Bar plot
# ax.bar(labels,counts)
# Bar plot theo cột ngang
ax.barh(labels,counts,color=colors)
plt.show()
