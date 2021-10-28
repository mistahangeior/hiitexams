import json
import random
from datetime import datetime


def write_file(db_path, users):
        with open(db_path, 'w') as file_write:
            json.dump(users, file_write)
            
def read_all_users(db_path):
        try:
            users = []
            with open(db_path, 'r') as users_file:
                users = json.load(users_file)
            return users
        except:
            users = []
            with open(db_path, 'w') as users_file:
                json.dump(users, users_file)
            return users
                

def read_user(db_path, email):
        users = read_all_users(db_path)
        if users != []:
            user = [user for user in users if user['email'] == email]
            if user != []:
                return user[0]
            else: 
                return 0
        else:
            return 0
            

def create_user(db_path, user_details):
        users = read_all_users(db_path)
        user = read_user(db_path, user_details['email'])
        if user == 0:
            user_details['id'] = "PAR-" + str(random.randint(000, 999))
            user_details['month'] = datetime.now().month
            users.append(user_details)
            write_file(db_path, users)
            return 1
        else:
            return 0
            

def update_user(db_path, email, **kwargs):
        user = read_user(db_path, email)
        if user != 0:
            users = read_all_users(db_path)
            users.remove(user)
            user['name'] = kwargs.get('name', user['name'])
            user['email'] =  kwargs.get('new_email', user['email'])            
            users.append(user)
            write_file(db_path, users)
            return 1
        else:
            return 0