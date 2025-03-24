from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost"
DB_NAME = "taskdatabase"


client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]




