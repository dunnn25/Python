import module

# print(f"__name__ in the run.py: {__name__}")

def my_func(c,d):
    print("c - d =", c-d)
    
if __name__ == "__main__":
    my_func(19,4)
    module.func(11,2)
    
# Khi thực hiện python file có code thực thi thì nên gom tất cả vào trong conditional statement để tránh thực thi các đoạn code mà mình không mong muốn