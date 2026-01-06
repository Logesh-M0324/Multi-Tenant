from fastapi import APIRouter

router = APIRouter(prefix="/admin/ai", tags=["AI Governance"])

@router.get("/decisions")
async def list_decisions():
    return []
