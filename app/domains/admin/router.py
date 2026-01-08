from fastapi import APIRouter, Depends
from domains.admin.schemas import TenantCreate, TenantUpdate
from domains.admin.service import AdminService
from core.dependencies import require_role
from core.database import get_db

router = APIRouter(prefix="/admin", tags=["Admin"])
service = AdminService()

# -----------------------------
# Tenant Management
# -----------------------------

@router.post("/tenants", dependencies=[Depends(require_role("ADMIN"))])
async def create_tenant(payload: TenantCreate, db=Depends(get_db)):
    print("Creating tenant")
    return await service.create_tenant(payload.name, payload.status)

@router.get("/tenants", dependencies=[Depends(require_role("ADMIN"))])
async def list_tenants():
    return await service.list_tenants()

@router.get("/tenants/{tenant_id}", dependencies=[Depends(require_role("ADMIN"))])
async def get_tenant(tenant_id: str):
    return await service.get_tenant(tenant_id)

@router.patch("/tenants/{tenant_id}", dependencies=[Depends(require_role("ADMIN"))])
async def update_tenant(tenant_id: str, payload: TenantUpdate):
    return await service.update_tenant(tenant_id, payload.status)

@router.delete("/tenants/{tenant_id}", dependencies=[Depends(require_role("ADMIN"))])
async def delete_tenant(tenant_id: str):
    await service.delete_tenant(tenant_id)
    return {"status": "deleted"}
