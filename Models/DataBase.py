import pymongo
from utility import UUID


class DBClient:
    client = pymongo.MongoClient("mongodb://127.0.0.1/", 1234, connect=False)
    database = client.get_database("App")

    database.command


    roles_collection = database["roles"]
    users_collection = database["users"]
    posts_collection = database["posts"]

    if not roles_collection.find_one({"_id": 1000000000000001}):
        permissions =  0b00000000000010000001
        roles_collection.insert_one({"_id": UUID.get_next_uuid("ROLE"), "name": "default", "permissions": permissions.value, "position": 0})

#if __name__ == "__main__":
    #DBClient.database.command(
    #    'createUser', 'User', 
    #pwd='123',
    #roles=[{'role': 'readWrite', 'db': 'App'}])