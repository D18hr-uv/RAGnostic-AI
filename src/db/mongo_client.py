"""
MongoDB client initialization.
"""

from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "ragnostic_ai"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
