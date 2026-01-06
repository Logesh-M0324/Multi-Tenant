# database.py
from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

client: AsyncIOMotorClient | None = None
db = None

async def connect_db():
    global client, db
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    print(f"Connected to MongoDB: {settings.DB_NAME}")

async def close_db():
    if client:
        client.close()

# ADD THIS FUNCTION:
async def get_db():
    if db is None:
        raise RuntimeError("Database not initialized. Ensure lifespan is running.")
    return db