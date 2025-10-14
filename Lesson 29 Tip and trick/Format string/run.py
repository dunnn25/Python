
# name = "Min"
# print("I am " + name)
# print("I am", name)

# # string modulo operator %
# name = "Min"
# weight = 9.9
# # my_str = "My name's %s. I am %s kg" %(name, weight)
# my_str = "My name's %s. I am %.2f kg" %(name, weight)

# print(my_str)

"""Method 2: .format()""" # Cũng phổ biến
# name = "Mit"
# loc = "Hanoi"

# # print("My name's {}, I am from {}".format(name,loc))
# print("My name's {0}, I am from {1}".format(name,loc))
# print("My name's {x}, I am from {y}".format(x=name,y=loc))

# dict = {"name": "Mit", "loc":"Hanoi"}
# print("My name's {dict[name]}, I am from {dict[loc]}".format(dict=dict))

# acc = 0.123456
# print("accuracy: {}".format(acc))
# print("accuracy: {:.4f}".format(acc))

"""Method 3: f string""" #Cực kì phổ biến - nên sử dụng
# name = "Min"
# loc = "Hanoi"
# print(f"My name's {name}, I am from {loc}")

"""Method 4: Template string""" # Không phổ biến mấy
from string import Template

name = "Linh"
t = Template("Hello, $name")
print(t.substitute(name=name))
