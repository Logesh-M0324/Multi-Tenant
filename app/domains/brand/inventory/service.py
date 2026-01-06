from domains.brand.inventory.repository import InventoryRepository

class InventoryService:
    def __init__(self):
        self.repo = InventoryRepository()

    async def list_inventory(self, tenant_id: str):
        return await self.repo.list(tenant_id)
