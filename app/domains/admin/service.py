from domains.admin.repository import AdminRepository
from shared.utils import generate_id

class AdminService:

    def __init__(self):
        self.repo = AdminRepository()

    async def create_tenant(self, name: str, status: str):
        tenant = {
            "tenant_id": generate_id(),
            "name": name,
            "status": status
        }
        print("Creating tenant in service:", tenant)
        return await self.repo.create_tenant(tenant)

    async def list_tenants(self):
        return await self.repo.list_tenants()

    async def get_tenant(self, tenant_id: str):
        return await self.repo.get_tenant(tenant_id)

    async def update_tenant(self, tenant_id: str, status: str):
        return await self.repo.update_tenant(tenant_id, {"status": status})

    async def delete_tenant(self, tenant_id: str):
        await self.repo.delete_tenant(tenant_id)
