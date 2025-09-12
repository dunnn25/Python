### Bài 1: Sử dụng map
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)