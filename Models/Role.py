from .DataBase import DBClient
from typing import Self
from .Permission import Permissions
from .User import User


class Role:
    @staticmethod
    def write_to_db(name: str, permissions: Permissions, position: int):
        role = {
            "name": name,
            "permissions_integer": permissions.value,
            "position": position
        }
        DBClient.roles_collection.insert_one(role)

    @staticmethod
    def get_by_name(name) -> dict:
        return DBClient.roles_collection.find_one({"name": name})
         

    @staticmethod
    def get_by_id(role_id: int) -> dict:
        return DBClient.roles_collection.find_one({"_id": int(role_id)})
