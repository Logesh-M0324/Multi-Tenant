from domains.admin.repository import AdminRepository
from shared.utils import generate_id

class AdminService:
    def __init__(self):
        self.repo = AdminRepository()

    async def create_tenant(self, name: str):
        tenant = {
            "_id": generate_id(),
            "name": name,
            "status": "ACTIVE"
        }
        await self.repo.create_tenant(tenant)
        return tenant
