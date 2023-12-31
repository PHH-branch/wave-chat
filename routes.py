'''
Defines routes functions for CRUD tasks.

Module Name: routes.py
Author: H
Date: September 7, 2023
'''

import sqlite3

from flask import request, jsonify

from app import app, db_connection
from models.chat_user import ChatUserModel, ChatUserValidator


@app.route('/')
def index():
    return 'Hello, Cosmos!'


@app.route('/users/', methods=['POST'])
@db_connection
def create_chat_user(conn, cursor):
    try:
        data = request.json
        ChatUserValidator.validate_create(data)
        ChatUserModel.create(conn, cursor, data)
        return jsonify({'message': 'User created'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 400


@app.route('/users/', methods=['GET'])
@db_connection
def get_chat_users(conn, cursor):
    chat_users = ChatUserModel.get(conn, cursor)
    return jsonify({'users': chat_users}), 200


@app.route('/users/<int:id>/', methods=['PUT'])
@db_connection
def update_chat_user(conn, cursor, id):
    try:
        data = request.json
        ChatUserValidator.validate_create(data)
        ChatUserModel.update(conn, cursor, id, data)
        return jsonify({'message': 'User updated'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 400


@app.route('/users/<int:id>/', methods=['GET'])
@db_connection
def get_chat_user_by_id(conn, cursor, id):
    chat_user = ChatUserModel.get_by_id(conn, cursor, id)
    if chat_user:
        return jsonify({'user': chat_user}), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/users/waveid/<int:wave_id>/', methods=['GET'])
@db_connection
def get_chat_user_by_wave_id(conn, cursor, wave_id):
    chat_user = ChatUserModel.get_by_wave_id(conn, cursor, wave_id)
    if chat_user:
        return jsonify({'user': chat_user}), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/users/phone/<phone>/', methods=['GET'])
@db_connection
def get_chat_user_by_phone(conn, cursor, phone):
    chat_user = ChatUserModel.get_by_phone(conn, cursor, phone)
    if chat_user:
        return jsonify({'user': chat_user}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
