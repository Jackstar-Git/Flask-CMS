from .DataBase import DBClient
from logging_utility import logger
from datetime import datetime
from utility import UUID

class User:
    @staticmethod
    def load_users() -> list:
        users = DBClient.users_collection.find()
        return list(users)

    @staticmethod
    def create_user(username: str, email: str, password: str, roles: list[dict]):
        data = {"_id": UUID.get_next_uuid("USER"),
                "username": username,
                'email': email, 
                'password': password,
                "created_at": datetime.timestamp(),
                "role_ids": [role.get("_id") for role in roles],
                "login_tries": 0
                }
        DBClient.users_collection.insert_one(data)
        logger.info("Successfully added the following user to the database: '%s'", email)

    @staticmethod
    def find_user_by_mail(email: str):
        query = {"email": email}
        result = DBClient.users_collection.find_one(query)
        return result
    
    @staticmethod
    def find_user_by_id(_id: int):
        query = {"_id": _id}
        print(query)
        result = DBClient.users_collection.find_one(query)
        
        return result

    @staticmethod
    def find_users_by_name(name: str) -> list:
        query = {"username": {"$regex": f"\\b\\w*{name}\\w*\\b", "$options": "i"}}
        result = DBClient.users_collection.find(query, {"password": 0})
        return list(result)
    
    @staticmethod
    def find_all_users(num) -> list:
        result = DBClient.users_collection.find({}, {"password": 0})
        return list(result)
    
    @staticmethod
    def delete_user(_id: str):
        query = {"_id": _id}
        DBClient.users_collection.delete_one(query)
    
    @staticmethod
    def update_user_data(_id: int, **new_values):
        query = {"_id": _id}
        newvalues = { "$set": new_values}

        DBClient.users_collection.update_one(query, newvalues)
