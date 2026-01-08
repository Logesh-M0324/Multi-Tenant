from domains.auth.repository import AuthRepository
from core.security import hash_password, verify_password, create_access_token

class AuthService:
    def __init__(self, database):
        self.repo = AuthRepository(database=database)
        print("hello from service")

    async def sign_up(self, email: str, password: str, tenant_id: str, role: str):
        existing = await self.repo.get_user_by_email(email)
        print(existing)
        if existing:
            raise Exception("User already exists")
        print("creating user")
        user = {
            "email": email,
            "password": hash_password(password),
            "tenant_id": tenant_id,
            "role": role
        }
        print("user to create:", user)
        return await self.repo.create_user(user)

    async def login(self, email: str, password: str):
        user = await self.repo.get_user_by_email(email)
        if not user or not verify_password(password, user["password"]):
            raise Exception("Invalid credentials")
        token_payload = {
            "user_id": str(user["_id"]),
            "tenant_id": user["tenant_id"],
            "role": user["role"]
        }
        access_token = create_access_token(token_payload)
        return {"access_token": access_token, "token_type": "bearer"}
