from core.database import db

class AuthRepository:

    def __init__(self, database):
        self.db = database
        print("hello from repository")

    async def create_user(self, user: dict):
        await self.db.users.insert_one(user)
        return user

    async def get_user_by_email(self, email: str):
        print("getting user by email from repo", self.db.users.find_one({"email": email}))
        return await self.db.users.find_one({"email": email})
