import sqlite3 

conn = sqlite3.connect('keys.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Keys (
               key_id INTEGER PRIMARY KEY AUTOINCREMENT,
               file_name TEXT UNIQUE NOT NULL, 
               key_value TEXT NOT NULL)
''')


conn.commit()
conn.close()