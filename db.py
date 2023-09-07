'''
Creates Sqlite database tables for Wave-Chat API.

Module Name: db.py
Author: H
Date: September 7, 2023
'''

import sqlite3

DATABASE = 'wave-chat.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# create ChatUser table
cursor.execute('''CREATE TABLE IF NOT EXISTS ChatUser
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   wave_id TEXT UNIQUE NOT NULL,
                   name TEXT,
                   phone TEXT UNIQUE NOT NULL,
                   device_info TEXT,
                   type INTEGET NOT NULL)''')

conn.commit()
conn.close()
