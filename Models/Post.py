from datetime import datetime
from .DataBase import DBClient
from .User import User
from logging_utility import logger
from utility import UUID

class Post:
    @staticmethod
    def load_posts() -> list:
        posts = DBClient.posts_collection.find()
        return list(posts)
    

    @staticmethod
    def create_post(title: str, author_id: str, categroy: str, content: str, tags: list[str]):
        data = {
                "_id": UUID.get_next_uuid("POST"),
                "title": title,
                "author": author_id,
                "content": content,
                "categroy": categroy,
                "tags": tags,
                "created_at": datetime.now(),
                "last_edit": datetime.now()
                }
        
        DBClient.posts_collection.insert_one(data)
        logger.info("Successfully created the following post: '%s'", title)

    @staticmethod
    def find_post_by_id(_id: int):
        query = {"_id": _id}
        result = DBClient.users_collection.find_one(query)
        return result

    @staticmethod
    def delete_post(_id: str):
        query = {"_id": _id}
        DBClient.users_collection.delete_one(query)