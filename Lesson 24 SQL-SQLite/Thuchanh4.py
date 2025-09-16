"""
UPDATE, DELETE trong SQLite

"""
import sqlite3
conn = sqlite3.connect('C:\\workspace\\30 Days of code the compelete python\\Lesson 23 SQL - SQLite\\example.db')
cursor = conn.cursor()
# # UPDATE
# cursor.execute("""
#                UPDATE STUDENTS
#                SET name = 'Phuc'
#                WHERE name = 'Cuong'""")

# DELETE
cursor.execute("""
               DELETE FROM STUDENTS
               WHERE name = 'Binh'
               """)
conn.commit()
conn.close()