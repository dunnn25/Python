# Biểu thức chình quy trong python giúp 
# Trích xuất các thông tin
# Validate format
# Thay thế các kiểu text
"""--------------------------"""
import re
# NOTE re.mach():Tìm kiếm ở đầu text 
# my_str = "Hello, nice to meet you"
# match = re.match("HelloABC",my_str)
# print(match)
# print(match.span())
# print(match.group())



# NOTE re.search(): Tìm kiếm ở bất kì vị trí cào
# my_str = "Hello, nice to meet you meet"
# match = re.search("meet",my_str)
# print(match)

# NOTE re.findall(): Trả về tất cả
# my_str = """Xin chao cac ban
# Chuc mung nam moi cac ban"""

# match = re.findall("ban",my_str)
# print(match)

# NOTE re.split():Chia đoạn text dựa trên chuỗi kí tự bất kì
my_str = "Xin chao cac ban, chao cac ban nhe"
# match = re.split(",",my_str)
match = re.split("cac",my_str,maxsplit=1) # Giới hạn số lần chia
print(match)
# NOTE re.sub(): Thay thế 1 hoặc nhiều các đoạn text bằng các đoạn text khắc trong string
my_str = "I love you. You love me too"
# # Thay tu love bằng từ hate
new_str = re.sub("love", "hate",my_str)
print(new_str)
