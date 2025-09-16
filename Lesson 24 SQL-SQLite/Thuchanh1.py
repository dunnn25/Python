import sqlite3

# tạo connection đến database
conn = sqlite3.connect('C:\\workspace\\30 Days of code the compelete python\\Lesson 23 SQL - SQLite\\example.db')
# tạo cursor object - lúc nào cũng cần tạo cái này trước khi chạy câu lệnh SQL
cursor = conn.cursor()


# Create table in DB, id, name, age, grade
cursor.execute("""
               CREATE TABLE IF NOT EXISTS STUDENTS (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER NOT NULL,
               grade TEXT
               )""")

# Commit changes - thuc su luu lai vao DB
conn.commit()
#.... tạo bằng, truy vấn ....
conn.close()
