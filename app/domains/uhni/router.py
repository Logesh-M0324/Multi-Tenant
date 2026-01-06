from fastapi import APIRouter, Depends
from core.dependencies import require_role

router = APIRouter(
    prefix="/uhni",
    tags=["UHNI"],
    dependencies=[Depends(require_role("UHNI"))]
)

@router.get("/profile")
async def profile():
    return {}
