from fastapi import APIRouter, Depends
from core.dependencies import require_role

router = APIRouter(
    prefix="/consumer",
    tags=["Consumer"],
    dependencies=[Depends(require_role("CONSUMER"))]
)

@router.get("/profile")
async def profile():
    return {}
