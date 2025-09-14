import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')  
arr_x =np.linspace(0,5,20)
arr_y =np.linspace(0,10,20)

fig, ax = plt.subplots()
ax.plot(arr_x,arr_y,marker='o', color='darkcyan', linestyle='--')
ax.set_xlabel('X-Axis')  # Thêm labels cho axis x,y 
ax.set_ylabel('Y-Axis')
ax.set_title('Matplotlib')
fig.suptitle('Line Plot', fontsize=16) # Thêm title cho figure
plt.show()