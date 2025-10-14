# if __name__ == "__main__":

# Sử dụng khi import các modules và để tránh thực thi các đoạn code không mong muốn
# __name__ trong file chạy có giá trị là "__main__"
# __name__ trong file được import có giá trị là tên của file được import

# print(f"__name__ in the module.py: {__name__}")

def func(a,b):
    print("a + b =", a+b)
    
# func(4,5)
if __name__ == "__main__":
    func(4,5)


