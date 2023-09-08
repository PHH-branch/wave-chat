'''
Creates Sqlite database tables for Wave-Chat API.

Module Name: db.py
Author: H
Date: September 7, 2023
'''

import random
import sqlite3
import string


def _create_name():
    letters = string.ascii_lowercase
    first_name = ''.join(random.choice(letters) for _ in range(4))
    last_name = ''.join(random.choice(letters) for _ in range(4))
    return f'{first_name.title()} {last_name.title()}'


DATABASE = 'wave-chat.db'

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# ChatUser table
table_name = 'ChatUser'
cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   wave_id TEXT UNIQUE NOT NULL,
                   name TEXT,
                   phone TEXT UNIQUE NOT NULL,
                   device_info TEXT,
                   type INTEGET NOT NULL)''')


def _create_chat_user_data():
    return {
        'wave_id': random.randint(10000, 99999),
        'name': _create_name(),
        'phone': f'09{random.randint(100000, 999999)}',
        'device_info': random.choice(['android', 'ios']),
        'type': random.randint(1, 2),
    }


# insert 5 ChatUsers
from models.chat_user import ChatUserModel  # nopep8
for _ in range(5):
    data = _create_chat_user_data()
    ChatUserModel.create(conn, cursor, data)


conn.commit()
conn.close()
