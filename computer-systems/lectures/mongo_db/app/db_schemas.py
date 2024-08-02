from datetime import datetime

from pymongo import MongoClient

from app.definitions import DB_NAME, DB_CONNECT_URI


class MongoDBInitializer:
    def __init__(self, connection_uri: str, db_name: str):
        self.client = MongoClient(connection_uri)
        self.db = self.client[db_name]

    def _create_genre_collection(self):
        self.db.create_collection("Genre", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            }
        })
        self.db["Genre"].create_index("name", unique=True)

    def _create_certification_collection(self):
        self.db.create_collection("Certification", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            }
        })
        self.db["Certification"].create_index("name", unique=True)

    def _create_director_collection(self):
        self.db.create_collection("Director", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            }
        })
        self.db["Director"].create_index("name", unique=True)

    def _create_star_collection(self):
        self.db.create_collection("Star", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            }
        })
        self.db["Star"].create_index("name", unique=True)

    def _create_movie_collection(self):
        self.db.create_collection("Movie", validator={
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "year", "time", "imdb", "votes"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "year": {
                        "bsonType": "int",
                        "minimum": 1888,
                        "maximum": datetime.now().year + 1,
                        "description": "must be an integer and is required"
                    },
                    "time": {
                        "bsonType": "int",
                        "minimum": 1,
                        "description": "must be an integer and is required"
                    },
                    "imdb": {
                        "bsonType": "double",
                        "minimum": 0.0,
                        "maximum": 10.0,
                        "description": "must be a double between 0 and 10 and is required"
                    },
                    "votes": {
                        "bsonType": "int",
                        "minimum": 0,
                        "description": "must be an integer and is required"
                    },
                    "meta_score": {
                        "bsonType": ["double", "null"],
                        "description": "must be a double or null"
                    },
                    "gross": {
                        "bsonType": ["double", "null"],
                        "description": "must be a double or null"
                    },
                    "certification": {
                        "bsonType": "objectId",
                        "description": "must be an ObjectId and is required"
                    },
                    "description": {
                        "bsonType": "string",
                        "description": "must be a string"
                    },
                    "genres": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "objectId"
                        },
                        "description": "must be an array of ObjectId"
                    },
                    "directors": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "objectId"
                        },
                        "description": "must be an array of ObjectId"
                    },
                    "stars": {
                        "bsonType": "array",
                        "items": {
                            "bsonType": "objectId"
                        },
                        "description": "must be an array of ObjectId"
                    }
                }
            }
        })
        self.db["Movie"].create_index(
            [("name", 1), ("year", 1), ("time", 1), ("imdb", 1)],
            unique=True
        )
        self.db["Movie"].create_index([("name", 1)])
        self.db["Movie"].create_index([("name", -1)])
        self.db["Movie"].create_index([("year", 1)])
        self.db["Movie"].create_index([("year", -1)])
        self.db["Movie"].create_index([("time", 1)])
        self.db["Movie"].create_index([("time", -1)])
        self.db["Movie"].create_index([("imdb", 1)])
        self.db["Movie"].create_index([("imdb", -1)])

    def create_all_collections(self):
        self._create_genre_collection()
        self._create_certification_collection()
        self._create_director_collection()
        self._create_star_collection()
        self._create_movie_collection()


if __name__ == "__main__":
    db_initializer = MongoDBInitializer(DB_CONNECT_URI, DB_NAME)
    db_initializer.create_all_collections()
