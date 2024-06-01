from typing import Self

permission_values = {
        "read": 0b00000001,
        "write": 0b00000010,
        "delete": 0b00000100,
        "update": 0b000001000
    }


class Permissions:
    def __init__(self, identifiers: list[str] | int):
        if isinstance(identifiers, int):
            if 0b0000000 > identifiers > 0b00001111:
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
        return cls(0b00001111)

    @classmethod
    def none(cls) -> Self:
        return cls(0b00000000)
