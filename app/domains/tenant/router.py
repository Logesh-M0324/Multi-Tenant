from fastapi import APIRouter

router = APIRouter(prefix="/tenant", tags=["Tenant"])

@router.get("/{tenant_id}")
async def get_tenant(tenant_id: str):
    return {"tenant_id": tenant_id}
