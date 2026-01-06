from core.database import db
from shared.tenant import tenant_filter

class UHNIRepository:
    """
    Repository layer for UHNI domain.
    All queries are tenant-aware.
    """

    async def get_profile(self, tenant_id: str, user_id: str):
        """
        Get UHNI profile for a user within a tenant
        """
        query = tenant_filter(tenant_id)
        query["user_id"] = user_id
        return await db.uhni_profiles.find_one(query)

    async def update_profile(self, tenant_id: str, user_id: str, update_data: dict):
        """
        Update UHNI profile for a user within a tenant
        """
        query = tenant_filter(tenant_id)
        query["user_id"] = user_id
        await db.uhni_profiles.update_one(query, {"$set": update_data})
        return await self.get_profile(tenant_id, user_id)
