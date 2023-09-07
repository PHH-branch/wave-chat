'''
ChatUser data model and validation.

Module Name: chat_user.py
Author: H
Date: September 7, 2023
'''


from multiprocessing import Value


class ChatUserValidator:
    '''Defines the validation methods for ChatUser data.
    '''

    @staticmethod
    def validate_create(data):
        '''Validates the data on POST and PUT requests.

        Args:
            data (JSON): data to create or update.

        Raises:
            ValueError: is raised when required data are missing.
        '''
        if ('wave_id' not in data or 'name' not in data or 'phone' not in data or
                'device_info' not in data or 'type' not in data):
            raise ValueError('Missing required fields')


class ChatUserModel:
    '''Defines database related methods for ChatUser table. 
    '''

    @staticmethod
    def create(conn, cursor, data):
        cursor.execute("INSERT INTO ChatUser (wave_id, name, phone, device_info, type) VALUES (?, ?, ?, ?, ?)",
                       (data['wave_id'], data['name'], data['phone'], data['device_info'], data['type']))

    @staticmethod
    def get_by_id(conn, cursor, id):
        cursor.execute("SELECT * FROM ChatUser WHERE id=?", (id,))
        return cursor.fetchone()

    @staticmethod
    def get_by_wave_id(conn, cursor, wave_id):
        cursor.execute("SELECT * FROM ChatUser WHERE wave_id=?", (wave_id,))
        return cursor.fetchone()

    @staticmethod
    def get_by_phone(conn, cursor, phone):
        cursor.execute(
            "SELECT * FROM ChatUser WHERE phone=?", (phone,))
        return cursor.fetchone()

    @staticmethod
    def update(conn, cursor, id, data):
        cursor.execute("UPDATE ChatUser SET name=?, phone=?, type=? WHERE id=?",
                       (data['name'], data['phone'], data['type'], id,))
