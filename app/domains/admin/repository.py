from core.database import get_db

class AdminRepository:

    async def create_tenant(self, tenant: dict):
        db = await get_db()
        result = await  db.tenants.insert_one(tenant)

        tenant["_id"] = str(result.inserted_id)  # ✅ convert ObjectId
        print("Tenant created in repository:", tenant)
        return tenant

    async def list_tenants(self):
        db = await get_db()
        result = await db.tenants.find().to_list(100)
        for tenant in result:
            tenant["_id"] = str(tenant["_id"])  # ✅ convert ObjectId
        return result

    async def get_tenant(self, tenant_id: str):
        db = await get_db()
        tenant = await db.tenants.find_one({"tenant_id": tenant_id})

        if tenant:
            tenant["_id"] = str(tenant["_id"])  # ✅ convert ObjectId
        return tenant

    async def update_tenant(self, tenant_id: str, data: dict):
        db = await get_db()
        await db.tenants.update_one(
            {"tenant_id": tenant_id},
            {"$set": data}
        )
        return await self.get_tenant(tenant_id)

    async def delete_tenant(self, tenant_id: str):
        db = await get_db()
        await db.tenants.delete_one({"tenant_id": tenant_id})
