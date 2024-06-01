from .DataBase import DBClient
from typing import Self
from .Permission import Permissions


class Role:
    def __init__(self, name: str, permissions: Permissions, position: int):
        self.name = name
        self.permissions = permissions
        self.position = position

    def __lt__(self, other: Self) -> bool:
        return self.position < other.position

    def __gt__(self, other: Self) -> bool:
        return self.position > other.position

    def __eq__(self, other: Self) -> bool:
        return self.position == other.position

    def __repr__(self) -> str:
        return f"Role(name={self.name}, permission={self.permissions}, position={self.position})"

    def write_to_db(self):
        role = {
            "name": self.name,
            "permissions_integer": self.permissions.value,
            "position": self.position
        }
        DBClient.roles_collection.insert_one(role)

    def update_permissions(self, permissions: Permissions) -> None:
        setattr(self, "permissions", permissions)

    @classmethod
    def get_by_name(cls, name) -> Self:
        result = DBClient.roles_collection.find_one({"name": name})
        return Role(name=result["name"], permissions=result["permissions"], position=result["position"])

    @classmethod
    def get_by_id(cls, role_id) -> Self:
        result = DBClient.roles_collection.find_one({"_id": role_id})
        return Role(name=result["name"], permissions=result["permissions"], position=result["position"])
