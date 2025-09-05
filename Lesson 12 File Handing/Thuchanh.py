# """Read"""
# file_obj = open("Lesson 12 file handing\my_text.txt")
# content = file_obj.read()
# print(content)
# file_obj.close() # Đóng file thủ công deo bao gio dung

# context manager
with open("Lesson 12 file handing\my_text.txt")as file_obj: 
    content = file_obj.read()  # can use .readline()  or   .readlines()
    print(content)

# ghi đè file -Write-
with open("new_file.txt", "w")as f:
    f.write("I love you ")

# "a"-Append
with open("new_file.txt", "a")as f:
    f.write("\nDeo")

# "X" - Create 
with open("new_file1.txt", "x")as f:
    pass