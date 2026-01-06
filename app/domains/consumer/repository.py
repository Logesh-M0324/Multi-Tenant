from core.database import db
from shared.tenant import tenant_filter

class ConsumerRepository:
    """
    Repository layer for Consumer domain.
    Read-only access to availability, alternatives, and profile
    """

    async def get_profile(self, tenant_id: str, user_id: str):
        query = tenant_filter(tenant_id)
        query["user_id"] = user_id
        return await db.consumer_profiles.find_one(query)

    async def get_availability(self, tenant_id: str, sku_id: str):
        query = tenant_filter(tenant_id)
        query["sku_id"] = sku_id
        return await db.inventory.find_one(query)

    async def get_alternatives(self, tenant_id: str, sku_id: str):
        """
        Fetch alternative SKUs for a given SKU
        """
        query = tenant_filter(tenant_id)
        query["sku_id"] = {"$ne": sku_id}
        return await db.inventory.find(query).to_list(10)
