from pymongo import MongoClient
from utils.config import settings
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

# Collections
users_collection = db["users"]
otp_collection = db["otp"]