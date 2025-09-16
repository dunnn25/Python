import sqlite3

conn = sqlite3.connect('C:\\workspace\\30 Days of code the compelete python\\Lesson 23 SQL - SQLite\\example.db')
cursor = conn.cursor()

# Cot: id, name, age, grade
# Insert a record
# id - là khoá chính, tự động tăng
# cursor.execute("""
#                INSERT INTO students (name, age, grade)
#                VALUES ('Dung',20,'A3')""")

# THêm nhiều dòng cùng lúc
# Bước 1: Đi tạo list các tuple mỗi tuple ứng với 1 cột
my_list = [
    ('An', 19, 'A1'),
    ('Binh', 20, 'A2'),
    ('Cuong', 21, 'A3')]

# Bước 2: Dùng hàm executemany
cursor.executemany("""
                INSERT INTO students (name, age, grade)
                VALUES (?,?,?)""", my_list)

conn.commit()
conn.close()