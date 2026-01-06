from fastapi import APIRouter, Depends
from core.dependencies import require_role

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(require_role("ADMIN"))]
)

@router.get("/tenants")
async def list_tenants():
    return []
