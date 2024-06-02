import os
from dotenv import set_key
import hashlib
from logging_utility import logger


class UUID:
    env_path =".env"

    @staticmethod
    def load_uuid(uuid_type):
        try:
            print(int(os.getenv(f"LAST_{uuid_type}_UUID")))
            return int(os.getenv(f"LAST_{uuid_type}_UUID"))
        except:
            return 1000000000000000

    @classmethod
    def get_next_uuid(cls, uuid_type):
        new_uuid = str(cls.load_uuid(uuid_type) + 1)
        cls._save_uuid(uuid_type, new_uuid)
        return int(new_uuid)

    @classmethod
    def _save_uuid(cls, uuid_type, new_value):
        set_key(dotenv_path=cls.env_path, key_to_set=f"LAST_{uuid_type}_UUID", value_to_set=new_value)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

