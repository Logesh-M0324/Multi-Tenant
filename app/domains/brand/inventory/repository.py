from core.database import db

class InventoryRepository:
    async def list(self, tenant_id: str):
        return await db.inventory.find({"tenant_id": tenant_id}).to_list(100)
