"""
MongoDB connection singleton for Jan Suvidha Portal.
"""
from pymongo import MongoClient
from django.conf import settings

_client = None
_db = None


def get_db():
    """Get MongoDB database instance (singleton)."""
    global _client, _db
    if _db is None:
        _client = MongoClient(settings.MONGO_URI)
        _db = _client[settings.MONGO_DB_NAME]
    return _db


def get_collection(name):
    """Get a specific MongoDB collection."""
    return get_db()[name]
