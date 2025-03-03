import json
import os

DATA_FILE = 'user_data.json'
USERS_FILE = 'users.json'


def read_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
       
        return []


def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def read_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
       
        return {}

def write_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)


def user_exists(username):
    users = read_users()
    return username in users