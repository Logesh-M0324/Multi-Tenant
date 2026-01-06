from core.database import db

class UserRepository:
    async def get_user(self, user_id: str):
        return await db.users.find_one({"_id": user_id})
