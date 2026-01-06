from domains.tenant.repository import TenantRepository

class TenantService:
    def __init__(self):
        self.repo = TenantRepository()

    async def validate(self, tenant_id: str):
        return await self.repo.get_by_id(tenant_id)
