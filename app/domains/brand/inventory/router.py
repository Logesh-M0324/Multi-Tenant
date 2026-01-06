from fastapi import APIRouter, Depends
from core.dependencies import require_role, get_current_user

router = APIRouter(
    prefix="/brand/inventory",
    tags=["Brand Inventory"],
    dependencies=[Depends(require_role("BRAND"))]
)

@router.get("/")
async def list_inventory(user=Depends(get_current_user)):
    return []
