# import sqlite3 as s
# conn = sqlite3.connect("todo.db")
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS tasks(
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# priority INTEGER NOT NULL
# );''')

# tasks = [
#     ('My first task', 1),
#     ('My second task', 10),
#     ('My thrid task', 5),
# ]

# # Insetr data.
# c.executemany("INSERT INTO tasks (name, priority) VALUES (?, ?)", tasks),
        

# # fix changes
# conn.commit()
# # close connection.
# conn.close

# class Todo:
#     "Documentation."

#     def __init__(self):
#         self.conn = s.connect('todo.db')
#         self.c = self.conn.cursor()
#         self.create_table()

#     def create_table(self):
#         print("\n\nСоздание таблицы, если не содержится.\n\n")
#         self.c.execute('''CREATE TABLE IF NOT EXISTS tasks(
#             id INTEGER PRIMARY KEY,
#             name TEXT NOT NULL,
#             priority INTEGER NOT NULL
#             );''')
        
#     def add_task(self):

#         self.name = input("Name:")
#         self.prior = int(input("Priority:"))

#         self.c.execute("INSERT INTO tasks (name, priority) Values (?, ?)",
#             (self.name, self.prior))
#         self.conn.commit()

#     def close_conn(self):
#         self.conn.close()

# app = Todo()
# app.add_task()
# app.close_conn

# conn = s.connect('todo.db')
# c = conn.cursor()
# for row in c.execute("SELECT * FROM tasks"):
#     print(row)
#     for it in range(len(row)):
#         print(row[it], end = " _ ")
#     print()
#     print()
# conn.close()

# conn = s.connect('todo.db')
# c = conn.cursor()

# SHOW.
# c.execute("SELECT * FROM tasks")
# rows = c.fetchall()

# for row in rows:
#     print(row)

# # UPDATE.
# c.execute("UPDATE tasks SET priority = ? WHERE id = ?", (30, 1))
# conn.commit()

# DELETE.
# c.execute("DELETE FROM TASKS WHERE ID = ?", (1,))
# conn.commit()

# conn.close()

# import xml.etree.ElementTree as ET

# tree = ET.parse('books.xml')
# root = tree.getroot()
# print("The root tag is:", root.tag)
# for child in root:
#     print(child.tag, child.attrib['title'])
# for author in root.iter('author'):
#     print(author.text)
