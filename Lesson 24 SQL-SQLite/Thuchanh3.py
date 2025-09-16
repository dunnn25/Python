""""
TRÍCH XUẤT DATA TỪ BẢNG
"""
import sqlite3 
conn = sqlite3.connect('C:\\workspace\\30 Days of code the compelete python\\Lesson 23 SQL - SQLite\\example.db')
cursor = conn.cursor()

# # fetch all rows - lấy tất cả các hàng
# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()
# print(type(rows)) # list
# for row in rows:
#     print(row)
#     print(type(row)) # tuple

# fetch specific columns + điều kiện age > 20
cursor.execute("SELECT name, grade FROM students WHERE age > 20")
rows= cursor.fetchall()
print(rows)
conn.close()