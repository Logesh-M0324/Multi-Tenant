from fastapi import APIRouter

router = APIRouter(prefix="/internal", tags=["Internal"])

@router.post("/auth/verify")
async def verify():
    return {"valid": True}
