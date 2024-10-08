from typing import Self
from .DataBase import DBClient
from .User import User

permission_values = {
    "view_posts":         0b00000000000000000001,
    "create_posts":       0b00000000000000000010,
    "delete_posts":       0b00000000000000000100,
    "update_posts":       0b00000000000000001000,
    "delete_comments":    0b00000000000000010000,
    "create_comments":    0b00000000000000100000,
    "view_comments":      0b00000000000001000000,
    "view_users":         0b00000000000010000000,
    "create_users":       0b00000000000100000000,
    "delete_users":       0b00000000001000000000,
    "update_users":       0b00000000010000000000,
    "admin_access":       0b00000000100000000000,
    "manage_roles":       0b00000001000000000000,
    "file_uploads":       0b00000010000000000000,
    "file_management":    0b00000100000000000000,
    "template_editing":   0b00001000000000000000,
    "plugin_management":  0b00010000000000000000,
    "seo_settings":       0b00100000000000000000,
    "analytics_access":   0b01000000000000000000,
    "password_recovery":  0b10000000000000000000
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
        return cls(0b11111111111111111111)

    @classmethod
    def none(cls) -> Self:
        return cls(0b00000000000000000000)

    @classmethod
    def admin(cls) -> Self:
        return cls(0b10000000111111111111)

    @classmethod
    def content_management(cls) -> Self:
        return cls(0b0000000000011111111)

    @classmethod
    def user_management(cls) -> Self:
        return cls(0b00000000011110000000)

    @classmethod
    def default(cls) -> Self:
        return cls(0b00000000000010100001)

    
    @staticmethod   
    def get_user_permissions(user_id: int)-> list:
        user = User.find_user_by_id(user_id)
        roles = DBClient.roles_collection.find({"_id": {"$in": user["role_ids"]}})
        permissions = [role["permissions"] for role in roles]
        return permissions
    
    @staticmethod
    def permission_check(permissions_to_check: list[int], permission_to_have: int) -> bool:
        return any([bool(permission & permission_to_have) for permission in permissions_to_check])
    

