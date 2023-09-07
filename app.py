'''
Entry file for wave-chat api.

Module Name: app.py
Author: H
Date: September 7, 2023
'''

import sqlite3
from functools import wraps

from flask import Flask

import db

app = Flask(__name__)


def db_connection(fn):
    '''Decorator function that handles opening and
    closing DB connection for each api request.
    '''
    @wraps(fn)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(db.DATABASE)
        cursor = conn.cursor()
        result = fn(conn, cursor, *args, **kwargs)
        conn.commit()
        conn.close()
        return result
    return wrapper


# circular import
from routes import *  # nopep8
