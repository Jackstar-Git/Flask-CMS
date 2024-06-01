import pymongo


class DBClient:
    client = pymongo.MongoClient("mongodb://127.0.0.1/", 1234, connect=False)
    database = client.get_database("App")

    roles_collection = database["roles"]
    users_collection = database["users"]
    posts_collection = database["posts"]
