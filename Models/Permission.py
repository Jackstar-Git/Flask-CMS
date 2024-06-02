from typing import Self
from .DataBase import DBClient
from .User import User

permission_values = {
        "view_posts": 0b00000001,
        "create_posts":0b00000010,
        "delete": 0b00000100,
        "update": 0b000001000,
        "delete_users": 0b000010000,
        "admin": 0b100000000
    }


class Permissions:
    def __init__(self, identifiers: list[str] | int):
        if isinstance(identifiers, int):
            if 0b0000000 > identifiers > 0b000011111:
                raise ValueError("This number is not within the allowed range!")
            self.value = identifiers
            return
        binary_value = 0
        for identifier in identifiers:
            if identifier not in permission_values:
                raise ValueError(f"Invalid permission identifier: {identifier}")
            binary_value |= permission_values[identifier]
        self.value = binary_value

    def get_permission_names(self):
        permission_names = []
        for name, value in permission_values.items():
            if self.value & value:
                permission_names.append(name)
        return permission_names

    def __eq__(self, other: Self) -> bool:
        return self.value == other.value

    def __repr__(self) -> str:
        return f"Permissions(value={self.value}, permissions={self.get_permission_names()})"

    @classmethod
    def all(cls) -> Self:
        return cls(0b111111111)

    @classmethod
    def none(cls) -> Self:
        return cls(0b000000000)
    
    @classmethod
    def default(cls) -> Self:
        return cls(0b000000011)
    
    @staticmethod   
    def get_user_permissions(user_id: int)-> list:
        user = User.find_user_by_id(user_id)
        roles = DBClient.roles_collection.find({"_id": {"$in": user["role_ids"]}})
        permissions = [role["permissions"] for role in roles]
        return permissions
    
    @staticmethod
    def permission_check(permissions_to_check: list[int], permission_to_have: int) -> bool:
        return any([bool(permission & permission_to_have) for permission in permissions_to_check])
    

