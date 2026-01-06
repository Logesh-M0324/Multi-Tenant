from core.database import db

class AdminRepository:
    async def create_tenant(self, tenant: dict):
        await db.tenants.insert_one(tenant)

    async def list_tenants(self):
        return await db.tenants.find().to_list(100)
