from domains.user.repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    async def get_profile(self, user_id: str):
        return await self.repo.get_user(user_id)
