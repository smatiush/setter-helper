import os
from dotenv import load_dotenv

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "false").lower() == "true"
DATABASE_NAME = os.getenv("DATABASE_NAME", "setter-helper")

if USE_MOCK:
    import mongomock
    client = mongomock.MongoClient()
else:
    from pymongo import MongoClient
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(MONGO_URI)
    print(f"Connect to MongoDB at {MONGO_URI}")

db = client[DATABASE_NAME]
