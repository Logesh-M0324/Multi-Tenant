from core.database import db

class TenantRepository:
    async def get_by_id(self, tenant_id: str):
        return await db.tenants.find_one({"_id": tenant_id})
